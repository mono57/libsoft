from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.layout.CommandFormWindow import Ui_CommandFormWidget
from views.add_command_article_view import AddCommandArticleView
from db.models import Provider, Command, CommandEntry, Article
from db.setup import Session, save


class CommandFormView(QDialog, Ui_CommandFormWidget):
    def __init__(self, articles, session, parent=None):
        super(CommandFormView, self).__init__(parent)
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Article', 'Quantité'])
        self.tableView.setModel(self.model)
        self.session = session

        self.providers = self.session.query(Provider).all()
        for provider in self.providers:
            self.comboBoxProvider.addItem(provider.full_name)

        self.articles = articles
        self.cmd_entries = []

    def compute_price(self):
        return sum([int(entry.article.selling_price)*int(entry.cmd_qte)
                    for entry in self.cmd_entries])

    def closeEvent(self, event):
        if self.cmd_entries:
            mBox = QMessageBox.question(
                self, "Avertissement",
                "Vous êtes sur le point d'enregistrer une commande. Si vous quittez, les données seront perdues \nVoulez vous vraiment quitter ?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if mBox == QMessageBox.Yes:
                super(CommandFormView, self).closeEvent(event)
            else:
                event.ignore()

    def entry_exist(self, designation):
        entry = [_entry for _entry in self.cmd_entries
                 if _entry.article.designation == designation]
        if entry:
            return entry[0]
        return False

    def update_total_price(self):
        total_price = self.compute_price()
        self.labelTotalCost.setText(str(total_price) + ' F CFA')

    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):
        add_cmd_article_win = AddCommandArticleView(articles=self.articles)
        add_cmd_article_win.exec_()

        form_data = add_cmd_article_win.get_form_data()

        if form_data:

            designation = form_data.get('designation')
            cmd_qte = int(form_data.get('qte'))

            article = [
                obj for obj in self.articles if obj.designation == designation][0]

            print('Type article : ', type(article))

            entry = self.entry_exist(designation)
            print("Entry type : ", type(entry))

            indexRow = 1

            if not entry:
                entry = CommandEntry(
                    cmd_qte=cmd_qte,
                    article=article
                )
                # entry.article = article
                self.cmd_entries.append(entry)
                indexRow = self.model.rowCount()

            else:
                entry.cmd_qte += cmd_qte
                index = self.cmd_entries.index(entry)
                indexRow = index
                self.cmd_entries[index] = entry

            self.session.add(entry)

            # print("Command Entry Article : ",
            #       entry.article.designation)
            # entry.article = article
            self.model.setItem(indexRow, 0, QStandardItem(
                entry.article.designation))
            self.model.setItem(indexRow, 1,
                               QStandardItem(str(entry.cmd_qte)))

            self.update_total_price()

    @pyqtSlot()
    def on_pushButtonAddCommand_clicked(self):
        if self.cmd_entries:
            provider_full_name = self.comboBoxProvider.currentText()

            if not self.cmd_entries:
                QMessageBox.information(
                    self, 'Info', 'Veuillez ajouter au moins un article à commander !', QMessageBox.Yes)
                return

            if not provider_full_name:
                mBox = QMessageBox.critical(
                    self, 'Attention !', 'Veuillez reseigner le champ fournisseur !', QMessageBox.Ok)
                if mBox == QMessageBox.Ok:
                    return

            _provider_instance = self.session.query(Provider).filter(
                Provider.full_name == provider_full_name).first()

            if not _provider_instance:
                mBox = QMessageBox.information(
                    self, 'Info', 'Le fournisseur que vous avez renseigné n\'existe pas dans la base de données. Voulez vous l\'enregistrer ?',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
                )
                if mBox == QMessageBox.No:
                    return

                _provider_instance = Provider(full_name=provider_full_name)

            command_instance = Command(
                motif=self.lineEditMotif.text(),
                emission_date=self.dateEditEmission.date().currentDate().toPyDate(),
                reception_date=self.dateEditReception.date().currentDate().toPyDate(),
                command_entries=self.cmd_entries
            )
            # print(_provider_instance)
            _provider_instance.commands.append(command_instance)

            self.session.add(command_instance)
            self.session.add(_provider_instance)

            self.session.commit()
            self.cmd_entries = []

    @pyqtSlot()
    def on_pushButtonDeleteArticle_clicked(self):
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

        for row in indexes:
            index = row.row()
            self.model.removeRow(index)
            return_value = self.cmd_entries.pop(index)
            if return_value:
                self.update_total_price()

    def close(self):
        self.session.close()
        super(CommandFormView, self).close()
