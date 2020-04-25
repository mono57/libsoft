from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.layout.MainWindow import Ui_MainWindow
from views.add_article_view import ArticleFormWindow
from db.setup import initDB

class MainWindowLib(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowLib, self).__init__(parent)
        self.setupUi(self)
        initDB()


    @pyqtSlot()
    def on_add_article_clicked(self):
        article_form_win = ArticleFormWindow()
        article_form_win.exec_()