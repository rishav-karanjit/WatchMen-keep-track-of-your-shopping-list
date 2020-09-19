from PyQt5 import QtWidgets, uic
import sys

from AddProduct import AddProductUI
from MainUI import MainUI

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
        self.dialog=AddProductUI()
        self.close()
    
    def NoAction(self):
        self.dialog=MainUI()
        self.close()