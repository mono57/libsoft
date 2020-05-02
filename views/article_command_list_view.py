from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from views.layout.ArticleCommandListWindow import Ui_ArticleCommandListWidget

from db.setup import Session
from db.models import CommandEntry, Article

class ArticleCommandListView(QDialog, Ui_ArticleCommandListWidget):
    def __init__(self, parent=None):
        super(ArticleCommandListView, self).__init__(parent)
        self.setupUi(self)
        self.session = Session()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Article', 'Quantité', 'Prix U.', 'Cout total'])

        self.entries = self.session.query(CommandEntry).all()
        for entry in self.entries:
            print('Article :', entry.article)

        self.session.close()


    def on_pushButtonQuit_clicked(self):
        self.close()