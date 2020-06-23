from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

from views.layout.InventaireWindow import Ui_InventaireWidget

class InventaireView(QDialog, Ui_InventaireWidget):
    def __init__(self, articles, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.articles = articles

        self.populate_comboBox(self.articles)

        self.checkBox.stateChanged.connect(self.on_checkBox_stateChanged)
        self.pushButton.clicked.connect(self.on_pushbutton_clicked)

        self.data = {}

    def get_return_data(self):
        
        return self.data

    def on_checkBox_stateChanged(self, checked):
        enabled = False if checked else True
        self.comboBox.setEnabled(enabled)

    def populate_comboBox(self, articles):
        for article in articles:
            self.comboBox.addItem(article.designation)

    def on_pushbutton_clicked(self):
        if self.checkBox.isChecked():
            self.data['all_article'] = True
        else:
            self.data['article'] = self.comboBox.currentText()

        self.close()
    
    def close(self):
        super().close()

