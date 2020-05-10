from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt

from views.layout.ArticleListWindow import Ui_ArticleListWidget
from db.models import Article
from db.setup import Session


class ArticleTableModel(QAbstractTableModel):

    def __init__(self, header, articles, *args):
        super(ArticleTableModel, self).__init__(*args)

        self.header = header
        self.articles_obj = articles
        self.articles = self.get_articles()

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

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return self.header[section]

    def add_articles(self, article_list_obj):
        article_list = [list(obj.values()) for obj in article_list_obj]
        self.articles += article_list

    def set_articles(self, article_list_obj):
        self.articles_obj = article_list_obj
        # self.add_articles(article_list_obj)
        self.articles = self.get_articles()

    def get_articles(self):
        
        article_list = []
        for article_obj in self.articles_obj:
            _article = [
                article_obj.code,
                article_obj.designation,
                article_obj.family,
                article_obj.author,
                article_obj.editor,
                article_obj.buying_price,
                article_obj.selling_price,
                str(article_obj.created_at),
                str(article_obj.quantity),
            ]
            article_list.append(_article)
        return article_list

class ArticleListView(QDialog, Ui_ArticleListWidget):
    def __init__(self, parent=None):
        super(ArticleListView, self).__init__(parent)
        self.setupUi(self)

        self.session = Session()

        self.articles = self.session.query(Article).all()
        self.header = ['Code', 'Designation', 'Famille',
                       'Auteur', 'Editeur', 'Prix d\'achat (F CFA)',
                       'Prix de vente (F CFA)', 'Date d\'ajout', 'Quantité en Stock']

        self.model = ArticleTableModel(self.header, self.articles)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()

    def close(self):
        self.session.close()
        super().close()