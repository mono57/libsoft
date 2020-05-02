from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.layout.CommandListWindow import Ui_CommandListWidget
from db.setup import Session
from db.models import Command

class CommandListView(QDialog, Ui_CommandListWidget):
    def __init__(self, parent=None):
        super(CommandListView, self).__init__(parent)
        self.setupUi(self)
        self.session = Session()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Article', 'Quantité', 'Prix U.', 'Cout total'])

        self.commands = self.session.query(Command).all()
