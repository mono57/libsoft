from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIntValidator
from views.layout.ArticleFormWindow import Ui_ArticleForm
from db.models import Article
from db.setup import save
import datetime


class ArticleFormWindow(QDialog, Ui_ArticleForm):
    def __init__(self, session, data=None, parent=None):
        super(ArticleFormWindow, self).__init__(parent)

        self.session = session
        self.setupUi(self)
        self.inputs_data_list = []
        self.form = {
            'isValid': False,
        }

        self.data = data

        if self.data is not None:
            self.spinBoxQteStock.setEnabled(True)
            self.pushButtonSave.setEnabled(False)
            self.populate_data_to_form()

        self.lineEditBuyPrice.setValidator(QIntValidator())
        self.lineEditSellingPrice.setValidator(QIntValidator())
        # self.lineEditCode.text()

    def populate_data_to_form(self):
        self.lineEditCode.setText(self.data.code)
        self.lineEditDesignation.setText(self.data.designation)
        self.lineEditAuthor.setText(self.data.author)
        self.lineEditBuyPrice.setText(self.data.buying_price)
        self.lineEditSellingPrice.setText(self.data.selling_price)

        self.comboBoxFamilly.setCurrentIndex(
            self.comboBoxFamilly.findText(self.data.family, Qt.MatchFixedString))
        
        self.comboBoxEditor.setCurrentIndex(
            self.comboBoxEditor.findText(self.data.editor, Qt.MatchFixedString))
        
        self.spinBoxQteStock.setValue(self.data.quantity)

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
        values['author'] = self.lineEditAuthor.text()
        values['buying_price'] = self.lineEditBuyPrice.text()
        values['selling_price'] = self.lineEditSellingPrice.text()
        values['editor'] = self.comboBoxEditor.currentText()
        values['qte_stock'] = self.spinBoxQteStock.value()
        values['date_add'] = datetime.date.today()
        return values

    def clear_inputs(self):
        self.lineEditCode.clear()
        self.lineEditDesignation.clear()
        self.lineEditBuyPrice.clear()
        self.lineEditSellingPrice.clear()
        # self.comboBoxFamilly.clear()
        # self.lineEditAuthor.clear()
        # self.comboBoxEditor.clear()
        self.spinBoxQteStock.clear()

    def values_changed(self, old_values, new_values):
        pass

    def save(self):
        inputs_values = self.get_inputs_values()

        if self.data:
            self.data.code = inputs_values.get('code')
            self.data.designation = inputs_values.get('designation')
            self.data.family = inputs_values.get('familly')
            self.data.author = inputs_values.get('author')
            self.data.editor = inputs_values.get('editor')
            self.data.buying_price = inputs_values.get('buying_price')
            self.data.selling_price = inputs_values.get('selling_price')
            self.data.quantity = inputs_values.get('qte_stock')

            self.session.add(self.data)
            self.session.commit()
            inputs_values['id'] = self.data.id
        else:
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
        # if instance:
        #     return inputs_values
        return inputs_values

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
