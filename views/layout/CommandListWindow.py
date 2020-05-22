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
        self.pushButtonUpdate = QtWidgets.QPushButton(CommandListWidget)
        self.pushButtonUpdate.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout.addWidget(self.pushButtonUpdate)
        self.pushButtonDelete = QtWidgets.QPushButton(CommandListWidget)
        self.pushButtonDelete.setStyleSheet("color: rgb(238, 238, 236);\n"
"background-color: rgb(239, 41, 41);")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
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
        self.pushButtonUpdate.setText(_translate("CommandListWidget", "Modifier"))
        self.pushButtonDelete.setText(_translate("CommandListWidget", "Supprimer"))
        self.pushButtonQuit.setText(_translate("CommandListWidget", "Quitter"))

