from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from views.layout.SellingFormWindow import Ui_SellingFormWidget
from views.add_command_article_view import AddCommandArticleView
from db.models import SellingEntry, Selling, Article


class SellingFormView(QDialog, Ui_SellingFormWidget):
    def __init__(self, session, articles, selling=None, parent=None):
        super(SellingFormView, self).__init__(parent)
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Article', 'Quantité', 'Prix Unitaire', 'Prix Total'])
        self.tableView.setModel(self.model)

        self.selling = selling

        self.session = session

        self.articles = self.session.query(Article).all()

        self.selling_entries = []

        if self.selling is not None:
            self.populate_selling_entries()

        self.dateEditSellingDate.setDate(QDate.currentDate())
        self.checkBoxRabai.stateChanged.connect(self.on_checkBoxRabai_stateChanged)
        self.spinBoxRabai.valueChanged.connect(self.on_spinBoxRabai_valueChanged)

    def on_spinBoxRabai_valueChanged(self):
        self.update_total_price()

    def on_checkBoxRabai_stateChanged(self, value):
        if value:
            self.spinBoxRabai.setEnabled(True)
        else:
            self.spinBoxRabai.setEnabled(False)
        self.update_total_price()

    def populate_selling_entries(self):
        for indexRow, entry in enumerate(self.selling.selling_entries):
            self.model.setItem(indexRow, 0, QStandardItem(
                entry.article.designation))
            self.model.setItem(indexRow, 1,
                               QStandardItem(str(entry.selling_qte)))
            selling_price = entry.article.selling_price
            self.model.setItem(indexRow, 2,
                               QStandardItem(selling_price))
            self.model.setItem(indexRow, 3,
                               QStandardItem(str(entry.selling_qte * int(float(selling_price)))))

            article = entry.article
            article.quantity += entry.selling_qte
            self.session.add(article)

            self.selling_entries.append(entry)

        self.lineEditClient.setText(self.selling.client)
        self.dateEditSellingDate.setDate(QDate(self.selling.selling_date))

    def entry_exist(self, designation):
        entry = [_entry for _entry in self.selling_entries
                 if _entry.article.designation == designation]
        if entry:
            return entry[0]
        return False

    def update_total_price(self):
        total_price = sum([entry.selling_qte*int(float(entry.article.selling_price))
                           for entry in self.selling_entries])
        discount = 0

        if self.checkBoxRabai.isChecked():
            discount = self.spinBoxRabai.value()

        self.labelTotalSelling.setText(str(total_price - (total_price * discount)//100))

    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):
        add_article_win = AddCommandArticleView(articles=self.articles)
        add_article_win.exec_()

        form_data = add_article_win.get_form_data()

        if form_data:
            designation = form_data.get('designation')
            selling_qte = int(form_data.get('qte'))

            article = [
                obj for obj in self.articles if obj.designation == designation][0]

            if article.quantity < selling_qte:
                QMessageBox.critical(
                    self, 'Info', 'La quantité à vendre est plus grande que celle en stock', QMessageBox.Yes)
                return

            # print('Type article : ', type(article))

            entry = self.entry_exist(designation)
            # print("Entry type : ", type(entry))

            indexRow = 1

            if not entry:
                entry = SellingEntry(
                    selling_qte=selling_qte,
                    article=article
                )
                # entry.article = article
                self.selling_entries.append(entry)
                indexRow = self.model.rowCount()

            else:
                entry.selling_qte += selling_qte
                index = self.selling_entries.index(entry)
                indexRow = index
                self.selling_entries[index] = entry

            # article.quantity -= entry.selling_qte
            # self.session.add(article)
            self.session.add(entry)

            # # print("Command Entry Article : ",
            # #       entry.article.designation)
            # # entry.article = article
            self.model.setItem(indexRow, 0, QStandardItem(
                entry.article.designation))
            self.model.setItem(indexRow, 1,
                               QStandardItem(str(entry.selling_qte)))
            selling_price = entry.article.selling_price
            self.model.setItem(indexRow, 2,
                               QStandardItem(selling_price))
            self.model.setItem(indexRow, 3,
                               QStandardItem(str(entry.selling_qte * int(float(selling_price)))))

            self.update_total_price()

            if self.selling_entries:
                self.pushButtonSelling.setEnabled(True)
                self.pushButtonDeleteArticle.setEnabled(True)

    @pyqtSlot()
    def on_pushButtonDeleteArticle_clicked(self):
        indexes = self.tableView.selectedIndexes()

        if not indexes and self.selling_entries:
            QMessageBox.information(
                self, 'Info', "Veuillez selectionner au préalable un article !", QMessageBox.Yes)
            return

        if not indexes:
            return

        if len(indexes) >= 2:
            QMessageBox.information(
                self, 'Info', 'Impossible de faire une selection groupée !', QMessageBox.Yes)
            return

        for row in indexes:
            index = row.row()
            self.model.removeRow(index)
            return_value = self.selling_entries.pop(index)
            if return_value:
                self.update_total_price()

    def closeEvent(self, event):
        if self.selling_entries:
            mBox = QMessageBox.information(
                self, 'Info', "Vous êtes sur le point d'enregistrer une commande. Si vous quittez, les données seront perdues \nVoulez vous vraiment quitter ?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if mBox == QMessageBox.Yes:
                super().closeEvent(event)
            else:
                event.ignore()

    @pyqtSlot()
    def on_pushButtonSelling_clicked(self):
        client_name = self.lineEditClient.text()
        if not client_name:
            QMessageBox.information(
                self, 'Info', 'Veuillez renseigner le nom du client ', QMessageBox.Yes)
            self.lineEditClient.setFocus()
            return

        for entry in self.selling_entries:
            article = entry.article
            article.quantity -= entry.selling_qte
            self.session.add(article)

        selling_instance = Selling(
            client=client_name,
            selling_entries=self.selling_entries,
            selling_discount=self.spinBoxRabai.value(),
            selling_date=self.dateEditSellingDate.date().toPyDate()
        )

        self.session.add(selling_instance)
        self.session.commit()

        self.selling_entries = []

        QMessageBox.information(
            self, 'Info', 'Vente effectuée avec succès !', QMessageBox.Yes)
        self.close()

    @pyqtSlot()
    def on_pushButtonQuit_clicked(self):
        self.close()
