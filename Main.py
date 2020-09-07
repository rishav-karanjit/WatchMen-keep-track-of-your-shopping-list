from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() 
        uic.loadUi('Main.ui', self) 
        
        self.button1 = self.findChild(QtWidgets.QPushButton, 'AddProduct')
        self.button2 = self.findChild(QtWidgets.QPushButton, 'ProductLists')
        self.button3 = self.findChild(QtWidgets.QPushButton, 'DeleteProduct')

        self.show() 


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()