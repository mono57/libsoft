from views.layout.AddCommandArticleWindow import Ui_AddCommandArticleWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from db.setup import Session
from db.models import Article


class AddCommandArticleView(QDialog, Ui_AddCommandArticleWidget):
    def __init__(self,articles, parent=None):
        super(AddCommandArticleView, self).__init__(parent)
        self.setupUi(self)
        self.session = Session()
        self.articles = self.session.query(Article).all()
        self.article = {}
        for _article in self.articles:
            self.comboBoxArticle.addItem(_article.designation)

    def get_form_data(self):
        return self.article

    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):

        qte = self.spinBoxQteCommand.value()            

        self.article['designation'] = self.comboBoxArticle.currentText()
        self.article['qte'] = qte
    
        self.close()

    def close(self):
        self.session.close()
        super().close()