# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/selling-rapport.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SellingRapportWidget(object):
    def setupUi(self, SellingRapportWidget):
        SellingRapportWidget.setObjectName("SellingRapportWidget")
        SellingRapportWidget.resize(352, 235)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SellingRapportWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(SellingRapportWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align: \'center\';")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(SellingRapportWidget)
        self.label_4.setStyleSheet("color: rgb(52, 101, 164);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(SellingRapportWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dateEditStartPeriod = QtWidgets.QDateEdit(SellingRapportWidget)
        self.dateEditStartPeriod.setCalendarPopup(True)
        self.dateEditStartPeriod.setObjectName("dateEditStartPeriod")
        self.verticalLayout.addWidget(self.dateEditStartPeriod)
        self.label_3 = QtWidgets.QLabel(SellingRapportWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dateEditEndPeriod = QtWidgets.QDateEdit(SellingRapportWidget)
        self.dateEditEndPeriod.setCalendarPopup(True)
        self.dateEditEndPeriod.setObjectName("dateEditEndPeriod")
        self.verticalLayout.addWidget(self.dateEditEndPeriod)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButtonGenerate = QtWidgets.QPushButton(SellingRapportWidget)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.verticalLayout.addWidget(self.pushButtonGenerate)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SellingRapportWidget)
        QtCore.QMetaObject.connectSlotsByName(SellingRapportWidget)

    def retranslateUi(self, SellingRapportWidget):
        _translate = QtCore.QCoreApplication.translate
        SellingRapportWidget.setWindowTitle(_translate("SellingRapportWidget", "Rapport de ventes"))
        self.label.setText(_translate("SellingRapportWidget", "Génerer un rapport des ventes"))
        self.label_4.setText(_translate("SellingRapportWidget", "NB: La période de fin doit être supperieur à celle ce debut"))
        self.label_2.setText(_translate("SellingRapportWidget", "Choisissez la période de debut :"))
        self.label_3.setText(_translate("SellingRapportWidget", "Choisissez la période de fin :"))
        self.pushButtonGenerate.setText(_translate("SellingRapportWidget", "Génerer"))

