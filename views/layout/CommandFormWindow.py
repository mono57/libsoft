# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'command-form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommandFormWidget(object):
    def setupUi(self, CommandFormWidget):
        CommandFormWidget.setObjectName("CommandFormWidget")
        CommandFormWidget.resize(804, 528)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CommandFormWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(CommandFormWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(CommandFormWidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(CommandFormWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(CommandFormWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(CommandFormWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.dateEdit_2 = QtWidgets.QDateEdit(CommandFormWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit_2)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(CommandFormWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(CommandFormWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(CommandFormWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(CommandFormWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(CommandFormWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CommandFormWidget)
        QtCore.QMetaObject.connectSlotsByName(CommandFormWidget)

    def retranslateUi(self, CommandFormWidget):
        _translate = QtCore.QCoreApplication.translate
        CommandFormWidget.setWindowTitle(_translate("CommandFormWidget", "Nouvelle commande"))
        self.label.setText(_translate("CommandFormWidget", "Fournisseur de la commande :"))
        self.label_2.setText(_translate("CommandFormWidget", "Date émission :"))
        self.label_3.setText(_translate("CommandFormWidget", "Date réception prévue :"))
        self.pushButton_2.setText(_translate("CommandFormWidget", "Ajouter un article"))
        self.pushButton.setText(_translate("CommandFormWidget", "Supprimer"))
        self.label_4.setText(_translate("CommandFormWidget", "Total :"))
        self.label_5.setText(_translate("CommandFormWidget", "0,0 F CFA"))

