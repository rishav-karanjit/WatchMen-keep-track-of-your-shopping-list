from PyQt5 import QtWidgets, uic
import sys

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

        self.CheckPrice.clicked.connect(self.DispPrice)
        self.show()