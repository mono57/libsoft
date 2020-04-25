from PyQt5.QtWidgets import QDialog
from views.layout.CommandFormWindow import Ui_CommandFormWidget


class CommandFormView(QDialog, Ui_CommandFormWidget):
    def __init__(self, parent=None):
        super(CommandFormView, self).__init__(parent)
        self.setupUi(self)
