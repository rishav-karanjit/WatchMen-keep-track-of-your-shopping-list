from PyQt5 import QtWidgets, uic
import sys

import AddProduct
from ProductList import ProductListUI
from DeleteProduct import DeleteProductUI
class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Main.ui', self) 
        
        self.button_AddP = self.findChild(QtWidgets.QPushButton, 'AddProduct')
        self.button_PList = self.findChild(QtWidgets.QPushButton, 'ProductLists')
        self.button_DelP = self.findChild(QtWidgets.QPushButton, 'DeleteProduct')
        self.button_Dark = self.findChild(QtWidgets.QPushButton, 'DarkModeBtn')
        self.button_Light = self.findChild(QtWidgets.QPushButton, 'LightModeBtn')
        self.bgcolor=1

        self.button_AddP.clicked.connect(self.AddP)
        self.button_PList.clicked.connect(self.PList)
        self.button_DelP.clicked.connect(self.DelP)
        self.button_Dark.clicked.connect(self.SetBGDark)
        self.button_Light.clicked.connect(self.SetBGLight)
        self.show()

    def AddP(self):
        self.dialog=AddProduct.AddProductUI(self.bgcolor)
        self.close()

    def PList(self):
        self.dialog=ProductListUI(self.bgcolor)
        self.close()

    def DelP(self):
        self.dialog=DeleteProductUI(self.bgcolor)
        self.close()
    
    def SetBGDark(self):
        self.bgcolor=1
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:1, y2:1, stop:0 rgba(36, 39, 28, 255), stop:1 rgba(221, 209, 221, 255))")
    
    def SetBGLight(self):
        self.bgcolor=0
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:0.528409, y2:0.83, stop:0 rgba(89, 99, 96, 255), stop:1 rgba(198, 187, 198, 255))")

        