from PyQt5.QtWidgets import QDialog
from views.layout.ArticleSearchWindow import Ui_ArticleSearchForm

class ArticleSearchView(QDialog, Ui_ArticleSearchForm):
    def __init__(self, parent=None):
        super(ArticleSearchView, self).__init__(parent)
        self.setupUi()