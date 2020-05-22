# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/gen-pdf-processing.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenPdfWidget(object):
    def setupUi(self, GenPdfWidget):
        GenPdfWidget.setObjectName("GenPdfWidget")
        GenPdfWidget.resize(333, 77)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(GenPdfWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(GenPdfWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(GenPdfWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(GenPdfWidget)
        QtCore.QMetaObject.connectSlotsByName(GenPdfWidget)

    def retranslateUi(self, GenPdfWidget):
        _translate = QtCore.QCoreApplication.translate
        GenPdfWidget.setWindowTitle(_translate("GenPdfWidget", "PDF Processing"))
        self.label.setText(_translate("GenPdfWidget", "Generation du pdf en progression.........."))

