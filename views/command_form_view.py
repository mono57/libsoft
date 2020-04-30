from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.layout.CommandFormWindow import Ui_CommandFormWidget
from views.add_command_article_view import AddCommandArticleView
from db.models import Provider, Command, CommandEntry, Article

class CommandFormView(QDialog, Ui_CommandFormWidget):
    def __init__(self, parent=None):
        super(CommandFormView, self).__init__(parent)
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Article', 'Quantité'])
        self.tableView.setModel(self.model)
        self.cmd_articles = []

    def compute_price(self):
        return sum([int(cmd.get('article').selling_price)*int(cmd.get('qte'))
                    for cmd in self.cmd_articles])

    def closeEvent(self, event):
        if self.cmd_articles:
            mBox = QMessageBox.question(
                self, "Avertissement",
                "Vous êtes sur le point d'enregistrer une commande. Si vous quittez, les données seront perdues \nVoulez vous continuer ?",
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
            article = form_data.get('article')
            item_article = QStandardItem(article.designation)
            item_qte = QStandardItem(str(form_data.get('qte')))
            self.model.setItem(self.model.rowCount(), 0, item_article)
            self.model.setItem(self.model.rowCount()-1, 1, item_qte)
            self.cmd_articles.append(form_data)
            total_price = self.compute_price()
            self.labelTotalCost.setText(str(total_price) + ' F CFA')
