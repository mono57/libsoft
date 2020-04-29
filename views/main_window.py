from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt
from PyQt5.QtGui import QStandardItemModel
from views.layout.MainWindow import Ui_MainWindow
from views.add_article_view import ArticleFormWindow
from views.selling_form_view import SellingFormView
from views.article_search_view import ArticleSearchView
from views.article_command_list_view import ArticleCommandListView
from views.command_form_view import CommandFormView
from views.command_list_view import CommandListView
from db.setup import initDB, Session
from db.models import Article


class ArticleTableModel(QAbstractTableModel):

    def __init__(self, header, *args):
        super(ArticleTableModel, self).__init__(*args)
        self.articles = self.get_articles()
        print("Les articles : {}".format(list(self.articles)))
        self.header = header

    def rowCount(self, *args):
        return len(self.articles)

    def columnCount(self, *args):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return self.articles[index.row()][index.column()]
        return QVariant()

    def add_articles(self, article_list_obj):
        article_list = [ list(obj.values()) for obj in article_list_obj ]
        self.articles += article_list
        

    def get_articles(self):
        session = Session()
        articles = session.query(Article).all()
        session.close()
        article_list = []
        for article_obj in articles:
            _article = [
                article_obj.code,
                article_obj.designation,
                article_obj.family,
                article_obj.author,
                article_obj.buying_price,
                article_obj.selling_price,
            ]
            article_list.append(_article)

        return article_list


class MainWindowLib(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowLib, self).__init__(parent)
        self.setupUi(self)
        initDB()
        self.header = ['Code', 'Designation', 'Famille', 'Auteur', 'Prix d\'achat', 'Prix de vente']
        self.article_table_model = ArticleTableModel(header=self.header)
        # self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(['Name', 'Age', 'Sex', 'Add'])
        # self.article_table_model.setHorizontalHeaderLabels(self.header)
        
        self.tableView.setModel(self.article_table_model)
        self.tableView.resizeColumnsToContents()
        # self.tableView.setHorizontalHeader()

    @pyqtSlot()
    def on_add_article_clicked(self):
        article_form_win = ArticleFormWindow()
        article_form_win.exec_()
        form_data_obj = article_form_win.get_form_data()
        if form_data_obj:
            self.article_table_model.add_articles(form_data_obj)
            self.tableView.model().layoutChanged.emit()

    @pyqtSlot()
    def on_add_selling_clicked(self):
        selling_form_win = SellingFormView()
        selling_form_win.exec_()

    @pyqtSlot()
    def on_add_command_clicked(self):
        add_command = CommandFormView()
        add_command.exec_()

    @pyqtSlot()
    def on_show_command_clicked(self):
        show_command = CommandListView()
        show_command.exec_()

    @pyqtSlot()
    def on_show_command_article_clicked(self):
        show_command_article = ArticleCommandListView()
        show_command_article.exec_()
        