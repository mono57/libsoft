from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QDate

from views.layout.SellingRapportWindow import Ui_SellingRapportWidget


class SellingRapportView(QDialog, Ui_SellingRapportWidget):
    def __init__(self, parent=None):
        super(SellingRapportView, self).__init__(parent)

        self.setupUi(self)
        self.periods = {}

        self.dateEditStartPeriod.setDate(QDate.currentDate())
        self.dateEditEndPeriod.setDate(QDate.currentDate())
        # set date with today's date
        self.checkBoxPeriod.stateChanged.connect(self.on_checkBox_stateChanged)

    def on_checkBox_stateChanged(self, state):
        if state:
            self.dateEditStartPeriod.setEnabled(False)
            self.dateEditEndPeriod.setEnabled(False)
        else:
            self.dateEditStartPeriod.setEnabled(True)
            self.dateEditEndPeriod.setEnabled(True)

    def get_periods(self):
        return self.periods if self.periods else None

    @pyqtSlot()
    def on_pushButtonGenerate_clicked(self):
        if self.checkBoxPeriod.isChecked():
            self.periods['all_periods'] = True
            self.close()
            
        self.periods['start'] = self.dateEditStartPeriod.date().toPyDate()
        self.periods['end'] = self.dateEditEndPeriod.date().toPyDate()

        if self.periods.get('start') > self.periods.get('end'):
            QMessageBox.information(
                self, 'Info', 'Le date de debut doit être inferieure à celle de fin', QMessageBox.Yes)
            return

        self.close()
