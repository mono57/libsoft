from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from views.layout.ArticleSearchWindow import Ui_ArticleSearchForm

class ArticleSearchView(QDialog, Ui_ArticleSearchForm):
    def __init__(self, parent=None):
        super(ArticleSearchView, self).__init__(parent)
        self.setupUi(self)
        self.query = None
        
    def get_query(self):
        return self.query

    def get_input(self):
        self.query = self.lineEditQuery.text()

    def process_search(self):
        self.get_input()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.process_search()
            return
        super(ArticleSearchView, self).keyPressEvent(event)
    
    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        self.process_search()