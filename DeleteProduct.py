from PyQt5 import QtWidgets, uic
import sys

import MainUI
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='root',database='WatchMen')
cursor = db.cursor()

class DeleteProductUI(QtWidgets.QDialog):
    def __init__(self,bgcolor):
        self.bgcolor = bgcolor
        super(DeleteProductUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/DeleteProduct.ui', self) 
        
        if self.bgcolor == 1:
            self.setStyleSheet("background-color: rgb(115, 115, 115)")
        else:
            self.setStyleSheet("background-color: rgb(188, 188, 188)")
        
        self.PName = self.findChild(QtWidgets.QComboBox, 'PName')
        self.DelProduct_B = self.findChild(QtWidgets.QPushButton, 'DelProduct_B')
        self.Cancel = self.findChild(QtWidgets.QPushButton, 'Cancel')

        self.Cancel.clicked.connect(self.GoBack)
        self.DelProduct_B.clicked.connect(self.DelP)

        cursor.execute('SHOW TABLES')
        all_product = cursor.fetchall()

        for i in all_product:
            self.PName.addItem(i[0])
        
        self.show()
    
    def DelP(self):
        ProName = str(self.PName.currentText())
        cursor.execute("DROP TABLE {ProName}".format(ProName=ProName))
        self.dialog = MainUI.MainUI(self.bgcolor)
        self.close()

    def GoBack(self):
        self.dialog = MainUI.MainUI(self.bgcolor)
        self.close()