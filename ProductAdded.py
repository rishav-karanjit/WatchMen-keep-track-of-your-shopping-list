from PyQt5 import QtWidgets, uic
import sys

import MainUI
import AddProduct

class ProductAdded(QtWidgets.QDialog):
    def __init__(self,bgcolor):
        self.bgcolor = bgcolor
        super(ProductAdded, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/ProductAddedUI.ui', self)

        if self.bgcolor == 1:
            self.setStyleSheet("background-color: rgb(115, 115, 115)")
        else:
            self.setStyleSheet("background-color: rgb(188, 188, 188)")
        
        self.button_Yes = self.findChild(QtWidgets.QPushButton, 'YesButton')
        self.button_No = self.findChild(QtWidgets.QPushButton, 'NoButton')
        
        self.button_Yes.clicked.connect(self.YesAction)
        self.button_No.clicked.connect(self.NoAction)

        self.show()
    
    def YesAction(self):
        self.dialog=AddProduct.AddProductUI(self.bgcolor)
        self.close()
    
    def NoAction(self):
        self.dialog=MainUI.MainUI(self.bgcolor)
        self.close()