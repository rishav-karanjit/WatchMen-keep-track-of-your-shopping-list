from PyQt5 import QtWidgets, uic
import sys
from bs4 import BeautifulSoup
import requests
import threading
from pynotifier import Notification

from MainUI import MainUI

import mysql.connector


def Price():
    try:       
        cursor.execute('SHOW TABLES')
        product_data = cursor.fetchall()
        product_list = []

        for x in range(len(product_data)):
            product_name = product_data[x][0]
            product_list.append(product_name)
        product_Price_lists = []
        for name in product_list:
            cursor.execute('SELECT Price FROM {table}'.format(table=name))
            product_Price_lists.append(cursor.fetchone()[0])

        Dict = dict(zip(product_list, product_Price_lists))
        product_link_lists = []
        for name in product_list:
            cursor.execute('SELECT Product_Link FROM {table}'.format(table=name))
            product_link_lists.append(cursor.fetchone()[0])
        for link in product_link_lists:
            source0 = requests.get(link, headers={'User-agent': 'Chrome'})
            source = source0.text
            data = BeautifulSoup(source, 'lxml')
            if 'amazon.in' in link:
                price0 = data.find('span', class_='a-size-medium a-color-price priceBlockBuyingPriceString').text
                price = int(price0[2:].replace(',', '').replace('.', '')) / 100
            if 'flipkart.com' in link:
                price0 = data.find('div', class_='_1vC4OE').text
                price = int(price0[1:].replace(',', ''))
            for product in Dict:
                if Dict[product] == price:
                    s = product + " price increased"
                    Notification(
	                            title='WatchMen Notification',
                                description=s,
                                duration=60,                              # Duration in seconds
                                urgency=Notification.URGENCY_CRITICAL
                            ).send()
                    cursor.execute(f'UPDATE {product} SET Price={price}')
                    db.commit()
                else:
                    return
    except:
        print("error")

if __name__ == "__main__":
    db = mysql.connector.connect(host='localhost',user='root',password='root',database='WatchMen')
    cursor = db.cursor() 
    bgcolor=1
    app = QtWidgets.QApplication(sys.argv)
    p1 = threading.Thread(target=Price)
    p1.start()
    window = MainUI(bgcolor=1)
    app.exec_()