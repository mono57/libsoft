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
        self.tableView.setModel(self.model)
        self.comboBoxFilter.currentTextChanged.connect(
            self.comboBoxFilter_currentTextChanged)
        self.model.setHorizontalHeaderLabels(
            ['Fournisseur', 'Nombre d\'articles commandés', 'Cout total', 'Status'])

        self._filter_text = self.comboBoxFilter.currentText()
        self._filter = self.format_filter(self._filter_text)

        self.commands = self.get_filtered_commands(self._filter)

        self.populate_data_to_tableView(self.commands)

    def comboBoxFilter_currentTextChanged(self, text):
        _filter= self.format_filter(text)
        _data = self.get_filtered_commands(_filter)
        self.model.removeRows(0, self.model.rowCount())
        self.populate_data_to_tableView(_data)

    def get_filtered_commands(self, _filter):
        if _filter is not None:
            return self.session.query(Command).filter(
                Command.receptionned==_filter).all()
        else:
            return self.session.query(Command).all()

    def format_filter(self, filter_text):
        if filter_text == 'Réceptionnées':
            return True
        elif filter_text == 'Non réceptionnées':
            return False
        else:
            return None

    def format_status(self, status):
        return 'Receptionnée' if status == True else 'Non receptionnée'

    def populate_data_to_tableView(self, data):
        prices = []
        for index, command in enumerate(data):
            entries = command.command_entries
            price = self.compute_command_price(entries)
            prices.append(price)
            item_provider = QStandardItem(command.provider.full_name)
            item_articles = QStandardItem(str(len(entries)))
            item_cost = QStandardItem(str(price))
            item_status = QStandardItem(
                self.format_status(command.receptionned))

            self.model.setItem(index, 0, item_provider)
            self.model.setItem(index, 1, item_articles)
            self.model.setItem(index, 2, item_cost)
            self.model.setItem(index, 3, item_status)

        self.labelTotalCost.setText(str(sum(prices)) + ' F CFA')

    def compute_command_price(self, entries):
        return sum([ int(obj.article.selling_price) * obj.cmd_qte for obj in entries ])

    @pyqtSlot()
    def on_pushButtonQuit_clicked(self):
        self.close()
