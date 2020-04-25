from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt
from PyQt5.QtGui import QStandardItemModel
from views.layout.MainWindow import Ui_MainWindow
from views.add_article_view import ArticleFormWindow
from views.selling_form_view import SellingFormView
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

    def get_articles(self):
        session = Session()
        articles = session.query(Article).all()
        article_list = []
        for index, article_obj in enumerate(articles):
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
        # self.tableView.setHorizontalHeader()

    @pyqtSlot()
    def on_add_article_clicked(self):
        article_form_win = ArticleFormWindow()
        article_form_win.exec_()

    @pyqtSlot()
    def on_add_selling_clicked(self):
        selling_form_win = SellingFormView()
        selling_form_win.exec_()