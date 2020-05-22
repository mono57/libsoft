from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot

from views.layout.SellingHistoryWindow import Ui_SellingHistoryWidget
from views.selling_form_view import SellingFormView
from db.models import Selling, Article
from db.setup import Session
from views.utils import get_index_table, get_data_by_model_pk

from sqlalchemy import desc


class SellingHistoryView(QDialog, Ui_SellingHistoryWidget):
    def __init__(self, parent=None):
        super(SellingHistoryView, self).__init__(parent)
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            'ID Vente', 'Nb Articles', 'Rabai (%)', 'Cout Total', 'Client', 'Date Vente',
        ])
        self.tableView.setModel(self.model)

        self.session = Session()
        # self.sellings = self.session.query(Selling).all()

        self.comboBoxFilter.currentTextChanged.connect(
            self.comboBoxFilter_currentTextChanged)

        self._filter_text = self.comboBoxFilter.currentText()
        self._filter = self.format_filter(self._filter_text)

        # self.sellings = self.get_filtered_sellings(self._filter)
        self.sellings = self.session.query(
            Selling).order_by(desc(Selling.created_at)).all()

        self.populate_data_to_tableView(self.sellings)

    def comboBoxFilter_currentTextChanged(self, text):
        _filter = self.format_filter(text)
        _data = self.get_filtered_sellings(_filter)
        self.model.removeRows(0, self.model.rowCount())
        self.populate_data_to_tableView(_data)

    def get_filtered_sellings(self, _filter):
        if _filter is not None:
            return self.session.query(Selling).filter(
                Selling.archived == _filter).all()
        else:
            return self.session.query(Selling).all()

    def format_filter(self, filter_text):
        if filter_text == 'Archivées':
            return True
        elif filter_text == 'Non archivées':
            return False
        else:
            return None

    def format_status(self, status):
        return 'Archivée' if status == True else 'Non archivée'

    def populate_data_to_tableView(self, data):
        prices = []
        for index, selling in enumerate(data):
            entries = selling.selling_entries
            selling_discount = selling.selling_discount
            discount = int(selling_discount) if selling_discount else 0
            price = self.compute_selling_price(entries, discount)
            prices.append(price)

            item_id = QStandardItem(str(selling.id))
            item_articles = QStandardItem(str(len(entries)))
            item_cost = QStandardItem(str(price))
            item_client = QStandardItem(selling.client)
            item_discount = QStandardItem(selling.selling_discount)
            # item_status = QStandardItem(
            #     self.format_status(selling.archived))
            item_selling_date = QStandardItem(str(selling.selling_date))
            # item_reception_date = QStandardItem(str(selling.reception_date))

            self.model.setItem(index, 0, item_id)
            self.model.setItem(index, 1, item_articles)
            self.model.setItem(index, 2, item_discount)
            self.model.setItem(index, 3, item_cost)
            self.model.setItem(index, 4, item_client)
            # self.model.setItem(index, 4, item_status)
            self.model.setItem(index, 5, item_selling_date)

    def compute_selling_price(self, entries, discount):
        total_price = sum([int(float(obj.article.selling_price))
                           * obj.selling_qte for obj in entries])
        return total_price - total_price * discount//100

    @pyqtSlot()
    def on_pushButtonArchiveSelling_clicked(self):
        indexes = self.tableView.selectedIndexes()

        if not indexes:
            QMessageBox.information(
                self, 'Info', 'Veuillez selectionner une vente', QMessageBox.Yes)
            return

        if len(indexes) >= 2:
            QMessageBox.information(
                self, 'Info', 'Impossible d\'archiver plusieurs vente en même temps!', QMessageBox.Yes)
            return

        row = self.tableView.currentIndex().row()
        index = self.tableView.model().index(row, 0)

        selling = [sell for sell in self.sellings if sell.id ==
                   int(index.data())][0]

        if selling.archived:
            QMessageBox.information(
                self, 'Info', 'Cette vente a déjà été archivée !', QMessageBox.Yes)
            return

        box = QMessageBox.information(
            self, 'Info', 'Vous êtes sur le point d\'archiver la vente.\nUn retour en stock sera fait. \nVoulez vous continuer',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if box == QMessageBox.No:
            return

        selling.archived = True
        for entry in selling.selling_entries:
            article = entry.article
            article.quantity += entry.selling_qte
            self.session.add(article)
        self.session.add(selling)

        self.session.commit()

        item_status = QStandardItem(
            self.format_status(selling.archived))
        self.model.setItem(row, 4, item_status)

        QMessageBox.information(
            self, 'Info', 'Vente archivée avec succès !', QMessageBox.Yes)

    @pyqtSlot()
    def on_pushButtonUpdate_clicked(self):
        row, index = get_index_table(self, self.tableView)

        if not index and not row:
            return

        selling = get_data_by_model_pk(self.sellings, int(index.data()))

        articles = self.session.query(Article).all()
        selling_form_win = SellingFormView(
            session=self.session, articles=articles, selling=selling)
        selling_form_win.exec_()

    @pyqtSlot()
    def on_pushButtonDelete_clicked(self):
        indexes = self.tableView.selectedIndexes()

        if not indexes and self.cmd_entries:
            QMessageBox.information(
                self, 'Info', "Veuillez selectionner au préalable une vente !", QMessageBox.Yes)
            return

        if not indexes:
            return

        if len(indexes) >= 2:
            QMessageBox.information(
                self, 'Info', 'Impossible de faire une selection groupée !', QMessageBox.Yes)
            return

        mBox = QMessageBox.critical(
            self, 'Alerte', 'Voulez vous vraiment supprimer cette vente ?', QMessageBox.No | QMessageBox.Yes, QMessageBox.No)

        if mBox == QMessageBox.No:
            return

        row = self.tableView.currentIndex().row()
        index = self.tableView.model().index(row, 0)

        for _row in indexes:
            selling = get_data_by_model_pk(self.sellings, int(index.data()))

            for entry in selling.selling_entries:
                article = entry.article
                article.quantity += entry.selling_qte
                self.session.add(article)

            self.session.delete(selling)

            index_ = self.sellings.index(selling)
            self.sellings.pop(index_)
            # self.model.removeRow(index)

            self.session.commit()
            i = _row.row()
            self.model.removeRow(i)

    @pyqtSlot()
    def on_pushButtonQuit_clicked(self):
        self.close()
