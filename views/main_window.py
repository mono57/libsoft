from PyQt5.QtWidgets import QMainWindow, QMessageBox, QAction, QDesktopWidget, QFileDialog
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt
from PyQt5.QtGui import QStandardItemModel, QIcon


import xlrd
# from openpyxl import load_workbook
from sqlalchemy import and_
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
from views.gen_pdf_view import GenPDFView
from db.setup import initDB, Session
from db.models import Article, Selling, Command
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
        article_form_win = ArticleFormWindow(session=self.session)
        article_form_win.exec_()
        form_data_obj = article_form_win.get_form_data()
        if form_data_obj:
            self.article_table_model.add_articles(form_data_obj)
            self.emit_tableView_layout_change_event()
            self.articles = self.session.query(Article).all()

    def emit_tableView_layout_change_event(self):
        self.tableView.model().layoutChanged.emit()

    @pyqtSlot()
    def on_pushButtonImport_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            self, 'Ouvrir le fichier', '', 'Text files (*.xlsx)')[0]

        wb = xlrd.open_workbook(file_name)
        # sheet = wb.active
        # for row in sheet.iter_rows():
        #     for cell in row:
        #         print(cell.value, end=' ')
        #     print()

        # print(str(sheet.max_row))
        # print(str(sheet.max_column))

        sheet = wb.sheet_by_index(0)

        # # print(sheet.cell_value(0, 0))
        article_list = []
        for i in range(2, sheet.nrows):
            # for j in range(0, sheet.ncols):
            article = Article(
                code=sheet.cell_value(i, 0),
                designation=sheet.cell_value(i, 1),
                family=sheet.cell_value(i, 2),
                author=sheet.cell_value(i, 3),
                editor=sheet.cell_value(i, 4),
                selling_price=sheet.cell_value(i, 5),
            )
            article_list.append({
                'code': sheet.cell_value(i, 0),
                'designation': sheet.cell_value(i, 1),
                'familly': sheet.cell_value(i, 2),
                'author': sheet.cell_value(i, 3),
                'editor': sheet.cell_value(i, 4),
                'selling_price': sheet.cell_value(i, 5)
            })
            self.session.add(article)

        self.session.commit()

        self.articles = self.session.query(Article).all()
        self.article_table_model.add_articles(article_list)
        self.emit_tableView_layout_change_event()

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
    def on_pushButtonCmdRapport_clicked(self):
        sell_rapport_win = SellingRapportView()
        sell_rapport_win.exec_()
        periods = sell_rapport_win.get_periods()
        if periods is not None:
            commands = self.session.query(Command).all()

            if not periods.get('all_periods', False):
                commands = self.session.query(Command).filter(
                    and_(
                        Command.date_reception >= periods.get('start'),
                        Command.date_reception <= periods.get('end'))).all()

            if commands:
                header = ['Article', 'Quantité',
                          'Fournisseur', 'Date de vente', ]
                gen_pdf_win = GenPDFView(collection=commands, periods=periods, header=header)
                gen_pdf_win.exec_()
                QMessageBox.information(
                    self, 'Info', 'Votre fichier a été genéré avec succès', QMessageBox.Yes)
                return

            QMessageBox.information(
                self, 'Info', 'Aucune vente trouvée pour la génération du rapport', QMessageBox.Yes)

    @pyqtSlot()
    def on_selling_rapport_clicked(self):
        sell_rapport_win = SellingRapportView()
        sell_rapport_win.exec_()
        periods = sell_rapport_win.get_periods()
        if periods is not None:
            sellings = self.session.query(Selling).all()

            if not periods.get('all_periods', False):
                sellings = self.session.query(Selling).filter(
                    and_(
                        Selling.selling_date >= periods.get('start'),
                        Selling.selling_date <= periods.get('end'))).all()

            if sellings:
                gen_pdf_win = GenPDFView(collection=sellings, periods=periods)
                gen_pdf_win.exec_()
                QMessageBox.information(
                    self, 'Info', 'Votre fichier a été genéré avec succès', QMessageBox.Yes)
                return

            QMessageBox.information(
                self, 'Info', 'Aucune vente trouvée pour la génération du rapport', QMessageBox.Yes)

    def close(self):
        self.session.close()
        super(MainWindowLib, self).close()
