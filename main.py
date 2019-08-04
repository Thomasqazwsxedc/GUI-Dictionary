from PyQt5.QtWidgets import *
from ui_scripts.window import Ui_MainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())

