from PyQt5 import QtWidgets, uic
import sys

class DeleteProductUI(QtWidgets.QDialog):
    def __init__(self):
        super(DeleteProductUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/DeleteProduct.ui', self) 
               
        self.show()