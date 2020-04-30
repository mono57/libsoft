from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.layout.CommandFormWindow import Ui_CommandFormWidget
from views.add_command_article_view import AddCommandArticleView
from db.models import Provider, Command, CommandEntry, Article
from db.setup import Session, save


class CommandFormView(QDialog, Ui_CommandFormWidget):
    def __init__(self, parent=None):
        super(CommandFormView, self).__init__(parent)
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Article', 'Quantité'])
        self.tableView.setModel(self.model)
        self.session = Session()

        self.providers = self.session.query(Provider).all()
        for provider in self.providers:
            self.comboBoxProvider.addItem(provider.full_name)

        self.cmd_articles = []
        self.command_entries = []

    def compute_price(self):
        return sum([int(cmd.get('article').selling_price)*int(cmd.get('qte'))
                    for cmd in self.cmd_articles])

    def closeEvent(self, event):
        if self.cmd_articles:
            mBox = QMessageBox.question(
                self, "Avertissement",
                "Vous êtes sur le point d'enregistrer une commande. Si vous quittez, les données seront perdues \nVoulez vous vraiment quitter ?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if mBox == QMessageBox.Yes:
                super(CommandFormView, self).closeEvent(event)
            else:
                event.ignore()

    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):
        add_cmd_article_win = AddCommandArticleView()
        add_cmd_article_win.exec_()
        form_data = add_cmd_article_win.get_form_data()
        if form_data:

            designation = form_data.get('article')

            article = self.session.query(Article).filter(
                Article.designation == designation)[0]
            print("Article : ", article)
            item_article = QStandardItem(article.designation)
            item_qte = QStandardItem(str(form_data.get('qte')))

            # cmd_entry_instance = save(
            #     CommandEntry(
            #         cmd_qte = int(form_data.get('qte')),
            #         article = article
            #     )
            # )

            cmd_entry_instance = CommandEntry(
                cmd_qte=int(form_data.get('qte'))
            )
            cmd_entry_instance.article = article
            self.session.add(cmd_entry_instance)

            print("Command Entry : ", cmd_entry_instance)
            # cmd_entry_instance.article = article
            self.command_entries.append(cmd_entry_instance)
            self.model.setItem(self.model.rowCount(), 0, item_article)
            self.model.setItem(self.model.rowCount()-1, 1, item_qte)

            self.cmd_articles.append({'article': article, 'qte': form_data.get('qte')})

            total_price = self.compute_price()
            self.labelTotalCost.setText(str(total_price) + ' F CFA')

    @pyqtSlot()
    def on_pushButtonAddCommand_clicked(self):
        provider_full_name = self.comboBoxProvider.currentText()

        if not provider_full_name:
            mBox = QMessageBox.critical(self, 'Attention !', 'Veuillez reseigner le champ fournisseur !', QMessageBox.Ok)
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
            motif = self.lineEditMotif.text(),
            emission_date = self.dateEditEmission.date().currentDate().toPyDate(),    
            reception_date = self.dateEditReception.date().currentDate().toPyDate(),
            command_entries = self.command_entries
        )
        # print(_provider_instance)
        _provider_instance.commands.append(command_instance)

        self.session.add(command_instance)
        self.session.add(_provider_instance)

        self.session.commit()
        self.cmd_articles = []
        self.close()
    

    def close(self):
        self.session.close()
        super(CommandFormView, self).close()