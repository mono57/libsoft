from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from views.layout.SellingFormWindow import Ui_Form

class SellingFormView(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(SellingFormView, self).__init__(parent)
        self.setupUi(self)