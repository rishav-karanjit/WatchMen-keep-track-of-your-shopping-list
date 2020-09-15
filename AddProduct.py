from PyQt5 import QtWidgets, uic
import sys

class AddProductUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddProductUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Main.ui', self) 
               
        self.show()