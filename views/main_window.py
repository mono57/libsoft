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
from views.selling_rapport_view import SellingRapportView
from views.article_list_view import ArticleListView
from db.setup import initDB, Session
from db.models import Article
from views.table_model import ArticleTableModel


class MainWindowLib(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowLib, self).__init__(parent)
        self.setupUi(self)

        initDB()
        self.session = Session()

        self.header = ['Code', 'Designation', 'Famille',
                       'Auteur', 'Editeur', 'Prix d\'achat (F CFA)', 'Prix de vente (F CFA)', 'Date d\'ajout']

        self.articles = self.session.query(Article).all()

        self.article_table_model = ArticleTableModel(
            articles=self.articles, header=self.header)
        # self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(['Name', 'Age', 'Sex', 'Add'])
        # self.article_table_model.setHorizontalHeaderLabels(self.header)
        self.tableView.setModel(self.article_table_model)
        self.tableView.resizeColumnsToContents()
        # self.tableView.setHorizontalHeader()
        # self.toolBar.addAction(
        #     QAction(QIcon('img/interface.png'), 'Add', self))
        # self.showFullScreen()
        self.lineEditSearch.textChanged.connect(self.handleTextChanged)
        self.showMaximized()
        screen = QDesktopWidget().screenGeometry()
        width, height = screen.width(), screen.height()
        # print(width, height)

    def handleTextChanged(self, value):
        if not value:
            self.article_table_model.set_articles(self.articles)
            self.emit_tableView_layout_change_event()

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
    def on_pushButtonArticleStock_clicked(self):
        article_list_win = ArticleListView()
        article_list_win.exec_()

    @pyqtSlot()
    def on_add_selling_clicked(self):
        selling_form_win = SellingFormView(
            session=self.session, articles=self.articles)
        selling_form_win.exec_()
        self.emit_tableView_layout_change_event()

    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        query = self.lineEditSearch.text()

        if not query:
            self.lineEditSearch.setFocus()
            return

        search_results = [obj for obj in self.articles if query.lower() in (
            obj.designation + obj.author + obj.code + obj.editor + obj.family).lower()]
        print(search_results)
        if not search_results:
            QMessageBox.information(self, 'Recherche', 'Aucune donnée trouvée pour le mot clef: {}'.format(
                query), QMessageBox.Yes)
            return
        self.article_table_model.set_articles(search_results)
        self.emit_tableView_layout_change_event()

    @pyqtSlot()
    def on_add_command_clicked(self):
        add_command = CommandFormView(
            session=self.session, articles=self.articles)
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

    @pyqtSlot()
    def on_selling_rapport_clicked(self):
        sell_rapport_win = SellingRapportView()
        sell_rapport_win.exec_()
        periods = sell_rapport_win.get_periods()
        if periods is not None:
            print(periods)

    def close(self):
        self.session.close()
        super(MainWindowLib, self).close()
