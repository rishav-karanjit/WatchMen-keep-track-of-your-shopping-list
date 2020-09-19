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
            self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:1, y2:1, stop:0 rgba(36, 39, 28, 255), stop:1 rgba(221, 209, 221, 255))")
        else:
            self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:0.528409, y2:0.83, stop:0 rgba(89, 99, 96, 255), stop:1 rgba(198, 187, 198, 255))")
        
        self.button_Yes = self.findChild(QtWidgets.QPushButton, 'YesButton')
        self.button_No = self.findChild(QtWidgets.QPushButton, 'NoButton')
        
        self.button_Yes.clicked.connect(self.YesAction)
        self.button_No.clicked.connect(self.NoAction)

        self.show()
    
    def YesAction(self):
        self.dialog=AddProduct.AddProductUI(self.bgcolor)
        self.close()
    
    def NoAction(self):
        self.dialog=MainUI.MainUI()
        self.close()