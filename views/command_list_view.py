from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from views.layout.CommandListWindow import Ui_CommandListWidget


class CommandListView(QDialog, Ui_CommandListWidget):
    def __init__(self, parent=None):
        super(CommandListView, self).__init__(parent)
        self.setupUi(self)