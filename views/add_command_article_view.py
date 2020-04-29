from views.layout.AddCommandArticleWindow import Ui_AddCommandArticleWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from db.setup import Session
from db.models import Article

class AddCommandArticleView(QDialog, Ui_AddCommandArticleWidget):
    def __init__(self, parent=None):
        super(AddCommandArticleView, self).__init__(parent)
        self.setupUi(self)

        self.session = Session()
        self.articles = self.session.query(Article).all()
        print(self.articles)
        self.session.close()
        for index, _article in enumerate(self.articles):
            self.comboBoxArticle.addItem(_article.designation)
        
        self.session.close()

    def get_form_data(self):
        return self.article

    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):
        self.article = {
            'article_designation': self.comboBoxArticle.currentText(),
            'qte': self.spinBoxQteCommand.value()
        }
        print(self.article)
        self.close()
