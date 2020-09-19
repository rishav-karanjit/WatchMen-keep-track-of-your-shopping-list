from PyQt5 import QtWidgets, uic
import sys

from MainUI import MainUI
bgcolor=1
app = QtWidgets.QApplication(sys.argv)
window = MainUI(bgcolor=1)
app.exec_() 