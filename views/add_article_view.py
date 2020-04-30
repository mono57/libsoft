from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from views.layout.ArticleFormWindow import Ui_ArticleForm
from db.models import Article
from db.setup import save


class ArticleFormWindow(QDialog, Ui_ArticleForm):
    def __init__(self, parent=None):
        super(ArticleFormWindow, self).__init__(parent)

        self.setupUi(self)
        self.inputs_data_list = []
        self.form = {
            'isValid': False,

        }

        self.error_fields = {
            'lineEditCode': self.labelErrorCode,
            'lineEditDesignation': self.labelErrorDesignation,
            'lineEditBuyPrice': self.labelErrorBuyingPrice,
            'lineEditSellingPrice': self.labelErrorSellingPrice
        }
        
        self.lineEditBuyPrice.setValidator(QIntValidator())
        self.lineEditSellingPrice.setValidator(QIntValidator())
        # self.lineEditCode.text()
        

        self.lineEditCode.textChanged.connect(
            lambda: self.textChanged('lineEditCode'))
        self.lineEditDesignation.textChanged.connect(
            lambda: self.textChanged('lineEditDesignation'))
        self.lineEditBuyPrice.textChanged.connect(
            lambda: self.textChanged('lineEditBuyPrice'))
        self.lineEditSellingPrice.textChanged.connect(
            lambda: self.textChanged('lineEditSellingPrice'))

    def textChanged(self, field):
        pass
    #     if field == 'lineEditCode':
    #         if len(self.lineEditCode.text()) == 0:
    #             self.error_fields[field].setText('Champ requis !')

    def get_inputs_values(self):
        values = {}
        values['code'] = self.lineEditCode.text()
        values['designation'] = self.lineEditDesignation.text()
        values['familly'] = self.comboBoxFamilly.currentText()
        values['author'] = self.comboBoxAuthor.currentText()
        values['buying_price'] = self.lineEditBuyPrice.text()
        values['selling_price'] = self.lineEditSellingPrice.text()
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
    def on_lineEditCode_textChanged(self, *args):
        print(args)
        print("Somthing wrong")

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
