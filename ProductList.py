from PyQt5 import QtWidgets, uic
import sys
import mysql.connector
import MainUI

db = mysql.connector.connect(host='localhost',user='root',password='root',database='WatchMen')
cursor = db.cursor()

class ProductListUI(QtWidgets.QDialog):
    def __init__(self,bgcolor):
        self.bgcolor = bgcolor
        super(ProductListUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/ProductList.ui', self) 
        
        if self.bgcolor == 1:
            self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:1, y2:1, stop:0 rgba(36, 39, 28, 255), stop:1 rgba(221, 209, 221, 255))")
        else:
            self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.67, y1:0.943318, x2:0.528409, y2:0.83, stop:0 rgba(89, 99, 96, 255), stop:1 rgba(198, 187, 198, 255))")
        
        self.PName = self.findChild(QtWidgets.QComboBox, 'PName')
        self.ShowButton = self.findChild(QtWidgets.QPushButton, 'ShowButton')
        self.Price = self.findChild(QtWidgets.QLabel, 'Price')
        self.URLtext = self.findChild(QtWidgets.QPlainTextEdit, 'URLtext')
        self.Cancel = self.findChild(QtWidgets.QPushButton, 'Cancel')

        self.ShowButton.clicked.connect(self.DispPrice)
        self.Cancel.clicked.connect(self.GoBack)

        cursor.execute('SHOW TABLES')
        all_product = cursor.fetchall()

        for i in all_product:
            self.PName.addItem(i[0])
        self.show()

    def DispPrice(self):
        ProName = str(self.PName.currentText())
        cursor.execute("SELECT * FROM {ProName}".format(ProName=ProName))
        items = cursor.fetchone()

        self.Price.setText(str(items[1]))
        self.URLtext.insertPlainText(items[0])
    
    def GoBack(self):
        self.dialog = MainUI.MainUI()
        self.close()
