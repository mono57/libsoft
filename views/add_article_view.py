from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from views.layout.ArticleFormWindow import Ui_ArticleForm
from db.models import Article
from db.setup import save

class ArticleFormWindow(QDialog, Ui_ArticleForm):
    def __init__(self, parent=None):
        super(ArticleFormWindow, self).__init__(parent)

        self.setupUi(self)
        self.inputs_data_list = []
    
    def get_inputs_values(self):
        values = {}
        values['code'] = self.lineEditCode.text()
        values['designation'] = self.lineEditDesignation.text()
        values['buying_price'] = self.lineEditBuyPrice.text()
        values['selling_price'] = self.lineEditSellingPrice.text()
        values['familly'] = self.comboBoxFamilly.currentText()
        values['author'] = self.comboBoxAuthor.currentText()
        values['editor'] = self.comboBoxEditor.currentText()
        values['qte_stock'] = self.spinBoxQteStock.value()
        return values

    def clear_inputs(self):
        self.lineEditCode.clear()
        self.lineEditDesignation.clear()
        self.lineEditBuyPrice.clear()
        self.lineEditSellingPrice.clear()
        # self.comboBoxFamilly.clear()
        # self.comboBoxAuthor.clear()
        # self.comboBoxEditor.clear()
        self.spinBoxQteStock.clear()
        

    def save(self):
        inputs_values = self.get_inputs_values()
        instance = save(
            Article(
                code=inputs_values.get('code'),
                designation=inputs_values.get('designation'),
                family=inputs_values.get('familly'),
                author=inputs_values.get('author'),
                editor=inputs_values.get('editor'),
                buying_price=inputs_values.get('buying_price'),
                selling_price=inputs_values.get('selling_price'),
                quantity=inputs_values.get('qte_stock'),
            )
        )
        if instance:
            return inputs_values
        return None
            

    @pyqtSlot()
    def on_pushButtonSaveAndQuit_clicked(self):
        values = self.save()
        if values is not None:
            self.inputs_data_list.append(values)
            self.close()

    def get_form_data(self):
        return self.inputs_data_list

    @pyqtSlot()
    def on_pushButtonSave_clicked(self):
        values = self.save()
        if values is not None:
            self.clear_inputs()
            self.inputs_data_list.append(values)


    @pyqtSlot()
    def on_pushButtonQuit_clicked(self):
        self.close()
