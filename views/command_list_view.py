from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.layout.CommandListWindow import Ui_CommandListWidget
from db.setup import Session
from db.models import Command, Article
from views.utils import get_index_table, get_data_by_model_pk
from views.command_form_view import CommandFormView
from sqlalchemy import desc
import datetime


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
            ['No', 'Nb articles',  'Cout total','Motif', 'Fournisseur', 'Date de Reception'])

        self._filter_text = self.comboBoxFilter.currentText()
        self._filter = self.format_filter(self._filter_text)

        # self.commands = self.get_filtered_commands(self._filter)
        self.commands = self.session.query(
            Command).order_by(desc(Command.created_at)).all()
        self.populate_data_to_tableView(self.commands)

    def comboBoxFilter_currentTextChanged(self, text):
        _filter = self.format_filter(text)
        _data = self.get_filtered_commands(_filter)
        self.model.removeRows(0, self.model.rowCount())
        self.populate_data_to_tableView(_data)

    def get_filtered_commands(self, _filter):
        if _filter is not None:
            return self.session.query(Command).filter(
                Command.receptionned == _filter).all()
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
        # prices = []
        for index, command in enumerate(data):
            entries = command.command_entries
            price = self.compute_command_price(entries)
            # prices.append(price)
            item_provider = QStandardItem(command.provider.full_name)
            item_articles = QStandardItem(str(len(entries)))
            item_cost = QStandardItem(str(price))
            item_motif = QStandardItem(command.motif)
            # item_emission_date = QStandardItem(str(command.emission_date))
            # item_reception_date = QStandardItem(str(command.reception_date))
            item_id = QStandardItem(str(command.id))
            item_date_recep = QStandardItem(str(command.date_reception))

            self.model.setItem(index, 0, item_id)
            self.model.setItem(index, 1, item_articles)
            self.model.setItem(index, 2, item_cost)
            self.model.setItem(index, 3, item_motif)
            # self.model.setItem(index, 4, item_emission_date)
            # self.model.setItem(index, 5, item_reception_date)
            self.model.setItem(index, 4, item_provider)
            self.model.setItem(index, 5, item_date_recep)

        # self.labelTotalCost.setText(str(sum(prices)) + ' F CFA')

    def compute_command_price(self, entries):
        return sum([int(float(obj.article.selling_price)) * obj.cmd_qte for obj in entries])

    @pyqtSlot()
    def on_pushButtonQuit_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pushButtonUpdate_clicked(self):
        row, index = get_index_table(self, self.tableView)

        if not index and not row:
            return

        command = [cmd for cmd in self.commands if cmd.id ==
                   int(index.data())][0]

        articles = self.session.query(Article).all()
        cmd_form_win = CommandFormView(
            articles=articles, session=self.session, command=command)
        cmd_form_win.exec_()

        # item_status = QStandardItem(
        #     self.format_status(command.receptionned))
        # self.model.setItem(row, 3, item_status)

        # QMessageBox.information(
        #     self, 'Info', 'Commande receptionnée avec succès !', QMessageBox.Yes)

        # self.close()
        # print(command.receptionned)

    @pyqtSlot()
    def on_pushButtonDelete_clicked(self):
        indexes = self.tableView.selectedIndexes()

        if not indexes and self.cmd_entries:
            QMessageBox.information(
                self, 'Info', "Veuillez selectionner au préalable un article !", QMessageBox.Yes)
            return

        if not indexes:
            return

        if len(indexes) >= 2:
            QMessageBox.information(
                self, 'Info', 'Impossible de faire une selection groupée !', QMessageBox.Yes)
            return

        mBox = QMessageBox.critical(
            self, 'Alerte', 'Voulez vous vraiment supprimer cette commande ?', QMessageBox.No | QMessageBox.Yes, QMessageBox.No)

        if mBox == QMessageBox.No:
            return

        row = self.tableView.currentIndex().row()
        index = self.tableView.model().index(row, 0)

        for _row in indexes:
            command = get_data_by_model_pk(self.commands, int(index.data()))

            for entry in command.command_entries:
                article = entry.article
                article.quantity -= entry.cmd_qte
                self.session.add(article)

            self.session.delete(command)

            index_ = self.commands.index(command)
            self.commands.pop(index_)
            # self.model.removeRow(index)

            self.session.commit()
            i = _row.row()
            self.model.removeRow(i)

    def close(self):
        self.session.close()
        super().close()
