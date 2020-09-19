from PyQt5 import QtWidgets, uic
import sys

import MainUI
import AddProduct

class ProductAdded(QtWidgets.QDialog):
    def __init__(self):
        super(ProductAdded, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/ProductAddedUI.ui', self) 

        self.button_Yes = self.findChild(QtWidgets.QPushButton, 'YesButton')
        self.button_No = self.findChild(QtWidgets.QPushButton, 'NoButton')
        
        self.button_Yes.clicked.connect(self.YesAction)
        self.button_No.clicked.connect(self.NoAction)

        self.show()
    
    def YesAction(self):
        self.dialog=AddProduct.AddProductUI()
        self.close()
    
    def NoAction(self):
        self.dialog=MainUI.MainUI()
        self.close()