# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/selling-history.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SellingHistoryWidget(object):
    def setupUi(self, SellingHistoryWidget):
        SellingHistoryWidget.setObjectName("SellingHistoryWidget")
        SellingHistoryWidget.resize(715, 434)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SellingHistoryWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SellingHistoryWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBoxFilter = QtWidgets.QComboBox(SellingHistoryWidget)
        self.comboBoxFilter.setObjectName("comboBoxFilter")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(SellingHistoryWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonUpdate = QtWidgets.QPushButton(SellingHistoryWidget)
        self.pushButtonUpdate.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout_2.addWidget(self.pushButtonUpdate)
        self.pushButtonDelete = QtWidgets.QPushButton(SellingHistoryWidget)
        self.pushButtonDelete.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(238, 238, 236);")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_2.addWidget(self.pushButtonDelete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonQuit = QtWidgets.QPushButton(SellingHistoryWidget)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout_2.addWidget(self.pushButtonQuit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SellingHistoryWidget)
        QtCore.QMetaObject.connectSlotsByName(SellingHistoryWidget)

    def retranslateUi(self, SellingHistoryWidget):
        _translate = QtCore.QCoreApplication.translate
        SellingHistoryWidget.setWindowTitle(_translate("SellingHistoryWidget", "Historique des ventes"))
        self.label.setText(_translate("SellingHistoryWidget", "Historique de toutes les ventes :"))
        self.comboBoxFilter.setItemText(0, _translate("SellingHistoryWidget", "Toutes les ventes"))
        self.comboBoxFilter.setItemText(1, _translate("SellingHistoryWidget", "Archivées"))
        self.comboBoxFilter.setItemText(2, _translate("SellingHistoryWidget", "Non archivées"))
        self.pushButtonUpdate.setText(_translate("SellingHistoryWidget", "Modifier"))
        self.pushButtonDelete.setText(_translate("SellingHistoryWidget", "Supprimer"))
        self.pushButtonQuit.setText(_translate("SellingHistoryWidget", "Quitter"))

