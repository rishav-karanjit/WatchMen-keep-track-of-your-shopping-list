from PyQt5 import QtWidgets, uic
import sys
from bs4 import BeautifulSoup
import requests

class AddProductUI(QtWidgets.QDialog):
    def __init__(self):
        super(AddProductUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/AddProduct.ui', self) 
        self.PName = self.findChild(QtWidgets.QLineEdit, 'PName')
        self.PLink = self.findChild(QtWidgets.QLineEdit, 'PLink')
        self.Save = self.findChild(QtWidgets.QPushButton, 'Save')
        self.Price= self.findChild(QtWidgets.QLabel,'Price')
        self.CheckPrice = self.findChild(QtWidgets.QPushButton, 'CheckPrice')

        self.CheckPrice.clicked.connect(self.DispPrice)
        self.Save.clicked.connect(self.SaveProduct)
        self.show()

    def DispPrice(self):
        ProName = self.PName.text()
        ProLink = self.PLink.text()
        if bool(ProLink):
            try:
                source0 = requests.get(ProLink,headers={'user-agent':'Chrome'})
                source = source0.text
                data = BeautifulSoup(source,'lxml')
                if 'amazon' in ProLink:
                    if(data.find('span',class_="a-size-medium a-color-price priceBlockDealPriceString")):
                        price0 = data.find('span',class_="a-size-medium a-color-price priceBlockDealPriceString").text
                    else:
                        price0 = data.find('span',class_="a-size-medium a-color-price priceBlockBuyingPriceString").text
                    self.Price.setText(price0)

                if 'flipkart.com' in ProLink:
                    price0 = data.find('div',class_="_1vC4OE _3qQ9m1").text
                    self.Price.setText(price0)
            except:
                self.Price.setText("Invalid URL")
                
    
    def SaveProduct(self):
        ProName = self.PName.text()
        ProLink = self.PLink.text()
        if bool(ProLink):
            try:
                source0 = requests.get(ProLink,headers={'user-agent':'Chrome'})
                source = source0.text
                data = BeautifulSoup(source,'lxml')
                if 'amazon.in' in ProLink:
                    if(data.find('span',class_="a-size-medium a-color-price priceBlockDealPriceString")):
                        price0 = data.find('span',class_="a-size-medium a-color-price priceBlockDealPriceString").text
                    else:
                        price0 = data.find('span',class_="a-size-medium a-color-price priceBlockBuyingPriceString").text
                    print(price0)

                if 'flipkart.com' in ProLink:
                    price0 = data.find('div',class_="_1vC4OE _3qQ9m1").text
                    print(price0)
                
            except:
                self.Price.setText("Invalid URL")

