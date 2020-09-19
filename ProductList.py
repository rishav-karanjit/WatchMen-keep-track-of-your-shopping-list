from PyQt5 import QtWidgets, uic
import sys
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='root',database='WatchMen')
cursor = db.cursor()

class ProductListUI(QtWidgets.QDialog):
    def __init__(self):
        super(ProductListUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/ProductList.ui', self) 
        
        self.PName = self.findChild(QtWidgets.QComboBox, 'PName')
        self.ShowButton = self.findChild(QtWidgets.QPushButton, 'ShowButton')
        self.Price = self.findChild(QtWidgets.QLabel, 'Price')
        self.URLtext = self.findChild(QtWidgets.QPlainTextEdit, 'URLtext')

        self.ShowButton.clicked.connect(self.DispPrice)

        cursor.execute('SHOW TABLES')
        all_product = cursor.fetchall()

        for i in all_product:
            self.PName.addItem(i[0])
        self.show()

    def DispPrice(self):
        ProName = str(self.PName.currentText())
        cursor.execute("SELECT * FROM {ProName}".format(ProName=ProName))
        items = cursor.fetchone()

        self.Price.setText(str(items[1]))
        self.URLtext.insertPlainText(items[0])
