from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot

from views.layout.SellingRapportWindow import Ui_SellingRapportWidget

class SellingRapportView(QDialog, Ui_SellingRapportWidget):
    def __init__(self, parent=None):
        super(SellingRapportView, self).__init__(parent)

        self.setupUi(self)
        self.periods = {}
        # set date with today's date

    def get_periods(self):
        return self.periods if self.periods else None

    @pyqtSlot()
    def on_pushButtonGenerate_clicked(self):
        self.periods['start'] = self.dateEditStartPeriod.date().currentDate().toPyDate()
        self.periods['end'] = self.dateEditEndPeriod.date().currentDate().toPyDate()

        self.close()