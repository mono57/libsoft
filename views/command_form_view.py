from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.layout.CommandFormWindow import Ui_CommandFormWidget
from views.add_command_article_view import AddCommandArticleView


class CommandFormView(QDialog, Ui_CommandFormWidget):
    def __init__(self, parent=None):
        super(CommandFormView, self).__init__(parent)
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Article', 'Quantité'])
        self.tableView.setModel(self.model)
        self.cmd_articles = []


    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):
        add_cmd_article_win = AddCommandArticleView()
        add_cmd_article_win.exec_()
        form_data = add_cmd_article_win.get_form_data()
        item_article = QStandardItem(form_data.get('article_designation'))
        item_qte = QStandardItem(str(form_data.get('qte')))
        self.model.setItem(self.model.rowCount(), 0, item_article)
        self.model.setItem(self.model.rowCount()-1, 1, item_qte)
        self.cmd_articles.append(form_data)




        
