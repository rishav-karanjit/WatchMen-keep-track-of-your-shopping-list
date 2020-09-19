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
            self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:1, y2:1, stop:0 rgba(36, 39, 28, 255), stop:1 rgba(221, 209, 221, 255))")
        else:
            self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:0.528409, y2:0.83, stop:0 rgba(89, 99, 96, 255), stop:1 rgba(198, 187, 198, 255))")
        
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
        self.dialog = MainUI.MainUI()
        self.close()

    def GoBack(self):
        self.dialog = MainUI.MainUI()
        self.close()