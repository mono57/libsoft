from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, QVariant, Qt

from views.layout.ArticleListWindow import Ui_ArticleListWidget
from views.add_article_view import ArticleFormWindow
from db.models import Article
from db.setup import Session
from views.utils import get_index_table, get_data_by_model_pk
from views.inventaire_view import InventaireView
from views.gen_pdf_view import GenPDFView

import sys


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
                article_obj.id,
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
        self.header = ['ID Article', 'Code', 'Designation', 'Famille',
                       'Auteur', 'Editeur', 'Prix d\'achat (F CFA)',
                       'Prix de vente (F CFA)', 'Date d\'ajout', 'Quantité en Stock']

        self.model = ArticleTableModel(self.header, self.articles)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.lineEditSearchQuery.textChanged.connect(self.handleTextChanged)


    def emit_tableView_layout_change_event(self):
        self.tableView.model().layoutChanged.emit()

    def handleTextChanged(self, value):
        if not value:
            self.model.set_articles(self.articles)
            self.emit_tableView_layout_change_event()

    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        query = self.lineEditSearchQuery.text()

        if not query:
            self.lineEditSearchQuery.setFocus()
            return

        search_results = [obj for obj in self.articles if query.lower() in (
            obj.designation + obj.author + obj.code + obj.editor + obj.family).lower()]

        if not search_results:
            QMessageBox.information(self, 'Recherche', 'Aucune donnée trouvée pour le mot clef: {}'.format(
                query), QMessageBox.Yes)
            return
        self.model.set_articles(search_results)
        self.emit_tableView_layout_change_event()

    @pyqtSlot()
    def on_pushButtonUpdate_clicked(self):
        row, index = get_index_table(self, self.tableView)

        if not index and not row:
            return

        article_id = index.data()
        article = get_data_by_model_pk(self.articles, int(article_id))
        # article = [ _article for _article in self.articles if _article.id == int(article_id) ][0]
        article_form_win = ArticleFormWindow(
            session=self.session, data=article)
        article_form_win.exec_()
        form_data = article_form_win.get_form_data()
        if form_data:
            # print(form_data)
            article = [obj for obj in self.articles if obj.id ==
                       form_data[0].get('id')][0]
            index = self.articles.index(article)
            self.articles[index] = article

            self.model.set_articles(self.articles)
            self.emit_tableView_layout_change_event()
            self.articles = self.session.query(Article).all()

    def close(self):
        self.session.close()
        super().close()

    @pyqtSlot()
    def on_pushButtonDelete_clicked(self):
        mBox = QMessageBox.critical(self, 'Avertissement',
                                    'Vous êtes sur le point de supprimer un article, continuer ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mBox == QMessageBox.Yes:
            print('Le Message Va être supprimer')

    @pyqtSlot()
    def on_pushButtonQuit_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pushButtonInventaire_clicked(self):
        inventaire_win = InventaireView(self.articles)
        inventaire_win.exec_()
        data = inventaire_win.get_return_data()

        if data:
            if data.get('all_article', False):
                collection = self.articles
            else:
                collection = [
                    article for article in self.articles if article.designation == data.get('article')]
                # print(collection[0].selling_entry)
            gen = GenPDFView(collection, is_inventaire=True)
            exit_code = gen.exec_()
            QMessageBox.information(
                self, 'Info', 'Votre fichier a été géneré avec succès !', QMessageBox.Yes)
