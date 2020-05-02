from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from views.layout.SellingFormWindow import Ui_Form
from views.add_command_article_view import AddCommandArticleView
from db.models import SellingEntry, Selling

class SellingFormView(QDialog, Ui_Form):
    def __init__(self,session, articles, parent=None):
        super(SellingFormView, self).__init__(parent)
        self.setupUi(self)

        self.session = session

    
    @pyqtSlot()
    def on_pushButtonAddArticle_clicked(self):
        add_article_win = AddCommandArticleView(articles = self.articles)
        add_article_win.exec_()

        form_data = add_article_win.get_article()
        
        if form_data:
            # designation = form_data.get('designation')
            # cmd_qte = int(form_data.get('qte'))

            # article = [
            #     obj for obj in self.articles if obj.designation == designation][0]

            # print('Type article : ', type(article))

            # entry = self.entry_exist(designation)
            # print("Entry type : ", type(entry))

            # indexRow = 1

            # if not entry:
            #     entry = SellingEntry(
            #         selling_qte=cmd_qte,
            #         article=article
            #     )
            #     # entry.article = article
            #     self.cmd_entries.append(entry)
            #     indexRow = self.model.rowCount()

            # else:
            #     entry.cmd_qte += cmd_qte
            #     index = self.cmd_entries.index(entry)
            #     indexRow = index
            #     self.cmd_entries[index] = entry

            # self.session.add(entry)

            # # print("Command Entry Article : ",
            # #       entry.article.designation)
            # # entry.article = article
            # self.model.setItem(indexRow, 0, QStandardItem(
            #     entry.article.designation))
            # self.model.setItem(indexRow, 1,
            #                    QStandardItem(str(entry.cmd_qte)))

            # self.update_total_price()
            pass