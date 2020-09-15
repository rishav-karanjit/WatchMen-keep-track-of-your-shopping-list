from PyQt5 import QtWidgets, uic
import sys

class ProductListUI(QtWidgets.QDialog):
    def __init__(self):
        super(ProductListUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/ProductList.ui', self) 
               
        self.show()