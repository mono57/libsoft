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
        self.tableView.setModel(self.model)
        self.cmd_articles = []
        # self.comboBoxFilter.currentTextChanged.connect(self.filterCurrentTextChanged)
        self.entries = self.session.query(CommandEntry).all()
        # print("Entries : ", self.entries)
        qtes = []
        for entry in self.entries:
            article = entry.article
            qte = entry.cmd_qte
            if article is not None:
                if article not in self.cmd_articles:
                    qtes.append(qte)
                    self.cmd_articles.append(article)
                else:
                    index = self.cmd_articles.index(article)
                    qtes[index] += qte

        i = 0
        for article in self.cmd_articles:
            selling_price = article.selling_price
            qte = qtes[i]

            item_designation = QStandardItem(article.designation)
            item_qte = QStandardItem(str(qte))
            item_price = QStandardItem(selling_price)
            item_total_price = QStandardItem(str(int(float(selling_price)) * int(qte)))

            self.model.setItem(i, 0,item_designation)
            self.model.setItem(i, 1,item_qte)
            self.model.setItem(i, 2,item_price)
            self.model.setItem(i, 3,item_total_price)

            i += 1

        self.labelTotalArticle.setText(str(len(self.cmd_articles)))

        self.session.close()

    def compute_total_price(self, entries):
        pass

    def filterCurrentTextChanged(self, text):
        print(text)
        

    def on_pushButtonQuit_clicked(self):
        self.close()