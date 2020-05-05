from PyQt5.QtWidgets import QMainWindow, QMessageBox, QAction, QDesktopWidget
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt
from PyQt5.QtGui import QStandardItemModel, QIcon
from views.layout.MainWindow import Ui_MainWindow
from views.add_article_view import ArticleFormWindow
from views.selling_form_view import SellingFormView
from views.article_search_view import ArticleSearchView
from views.article_command_list_view import ArticleCommandListView
from views.command_form_view import CommandFormView
from views.command_list_view import CommandListView
from views.selling_history_view import SellingHistoryView
from db.setup import initDB, Session
from db.models import Article


class ArticleTableModel(QAbstractTableModel):

    def __init__(self, header, articles, *args):
        super(ArticleTableModel, self).__init__(*args)

        self.header = header
        self.articles_obj = articles
        self.articles = self.get_articles()
        print('articles: ',articles)
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
        article_list = [list(obj.values()) for obj in article_list_obj]
        self.articles += article_list

    def set_articles(self, article_list_obj):
        self.articles = []
        self.add_articles(article_list_obj)

    def get_articles(self):
        
        article_list = []
        for article_obj in self.articles_obj:
            _article = [
                article_obj.code,
                article_obj.designation,
                article_obj.family,
                article_obj.author,
                article_obj.buying_price,
                article_obj.selling_price,
            ]
            article_list.append(_article)
        print("article list: ", article_list)
        return article_list


class MainWindowLib(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowLib, self).__init__(parent)
        self.setupUi(self)

        initDB()
        self.session = Session()

        self.header = ['Code', 'Designation', 'Famille',
                       'Auteur', 'Prix d\'achat', 'Prix de vente']

        self.articles = self.session.query(Article).all()

        self.article_table_model = ArticleTableModel(articles=self.articles, header=self.header)
        # self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(['Name', 'Age', 'Sex', 'Add'])
        # self.article_table_model.setHorizontalHeaderLabels(self.header)
        self.tableView.setModel(self.article_table_model)
        self.tableView.resizeColumnsToContents()
        # self.tableView.setHorizontalHeader()
        self.toolBar.addAction(QAction(QIcon('img/interface.png'), 'Add', self))
        # self.showFullScreen()
        self.showMaximized()
        screen = QDesktopWidget().screenGeometry()
        width, height = screen.width(), screen.height()
        # print(width, height)

    @pyqtSlot()
    def on_add_article_clicked(self):
        article_form_win = ArticleFormWindow()
        article_form_win.exec_()
        form_data_obj = article_form_win.get_form_data()
        if form_data_obj:
            self.article_table_model.add_articles(form_data_obj)
            self.emit_tableView_layout_change_event()
            self.articles = self.session.query(Article).all()


    def emit_tableView_layout_change_event(self):
        self.tableView.model().layoutChanged.emit()

    @pyqtSlot()
    def on_add_selling_clicked(self):
        selling_form_win = SellingFormView(session=self.session, articles=self.articles)
        selling_form_win.exec_()

    @pyqtSlot()
    def on_search_article_clicked(self):
        search_art_win = ArticleSearchView()
        search_art_win.exec_()
        query = search_art_win.get_query()

        if query:
            # articles = self.session.query(Article).all()

            search_results = [obj.__dict__ for obj in self.articles if query in (
                obj.designation or obj.author or obj.code or obj.editor or obj.family)]
            print(search_results)
            if not search_results:
                QMessageBox.information(self, 'Recherche', 'Aucune donnée trouvée pour le mot clef: {}'.format(
                    query), QMessageBox.Yes)
                return
            self.article_table_model.set_articles(search_results)
            self.emit_tableView_layout_change_event()

    @pyqtSlot()
    def on_add_command_clicked(self):
        add_command = CommandFormView(session=self.session, articles=self.articles)
        add_command.exec_()

    @pyqtSlot()
    def on_show_command_clicked(self):
        show_command = CommandListView()
        show_command.exec_()

    @pyqtSlot()
    def on_show_command_article_clicked(self):
        show_command_article = ArticleCommandListView()
        show_command_article.exec_()

    @pyqtSlot()
    def on_selling_history_clicked(self):
        selling_history = SellingHistoryView()
        selling_history.exec_()

    def close(self):
        self.session.close()
        super(MainWindowLib, self).close()
