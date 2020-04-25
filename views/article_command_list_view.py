from PyQt5.QtWidgets import QDialog
from views.layout.ArticleCommandListWindow import Ui_ArticleCommandListWidget


class ArticleCommandListView(QDialog, Ui_ArticleCommandListWidget):
    def __init__(self, parent=None):
        super(ArticleCommandListView, self).__init__(parent)
        self.setupUi(self)