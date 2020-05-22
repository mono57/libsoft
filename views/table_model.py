from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt
import datetime

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
        # article_list = [list(obj.values()) for obj in article_list_obj]
        article_list = []
        for article in article_list_obj:
            empty = ''
            article_list.append([
                article.get('code', empty),
                article.get('designation', empty),
                article.get('familly', empty),
                article.get('author', empty),
                article.get('editor', empty),
                article.get('buying_price', empty),
                article.get('selling_price', empty),
                article.get('buying_price', empty),
                str(article.get('date_add', datetime.date.today())),
            ])
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
                str(article_obj.created_at)
            ]
            article_list.append(_article)
        return article_list

