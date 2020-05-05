# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/command-list.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommandListWidget(object):
    def setupUi(self, CommandListWidget):
        CommandListWidget.setObjectName("CommandListWidget")
        CommandListWidget.resize(693, 422)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CommandListWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(CommandListWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(CommandListWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBoxFilter = QtWidgets.QComboBox(CommandListWidget)
        self.comboBoxFilter.setObjectName("comboBoxFilter")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxFilter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView = QtWidgets.QTableView(CommandListWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(CommandListWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.labelTotalCost = QtWidgets.QLabel(CommandListWidget)
        self.labelTotalCost.setObjectName("labelTotalCost")
        self.horizontalLayout.addWidget(self.labelTotalCost)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonReceptionned = QtWidgets.QPushButton(CommandListWidget)
        self.pushButtonReceptionned.setObjectName("pushButtonReceptionned")
        self.horizontalLayout.addWidget(self.pushButtonReceptionned)
        self.pushButtonQuit = QtWidgets.QPushButton(CommandListWidget)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout.addWidget(self.pushButtonQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CommandListWidget)
        QtCore.QMetaObject.connectSlotsByName(CommandListWidget)

    def retranslateUi(self, CommandListWidget):
        _translate = QtCore.QCoreApplication.translate
        CommandListWidget.setWindowTitle(_translate("CommandListWidget", "Form"))
        self.label_2.setText(_translate("CommandListWidget", "Toutes les commandes"))
        self.label.setText(_translate("CommandListWidget", "Filtrer par :"))
        self.comboBoxFilter.setItemText(0, _translate("CommandListWidget", "Toutes les commandes"))
        self.comboBoxFilter.setItemText(1, _translate("CommandListWidget", "Réceptionnées"))
        self.comboBoxFilter.setItemText(2, _translate("CommandListWidget", "Non réceptionnées"))
        self.label_3.setText(_translate("CommandListWidget", "Cout total des commandes :"))
        self.labelTotalCost.setText(_translate("CommandListWidget", "0,00 F CFA"))
        self.pushButtonReceptionned.setToolTip(_translate("CommandListWidget", "Marque une commande comme étant receptionnée"))
        self.pushButtonReceptionned.setText(_translate("CommandListWidget", "Marquer comme receptionnée"))
        self.pushButtonQuit.setText(_translate("CommandListWidget", "Quitter"))

