from PyQt5 import QtWidgets, uic
import sys

from MainUI import MainUI

app = QtWidgets.QApplication(sys.argv)
window = MainUI()
app.exec_()