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
        self.comboBoxProvider = QtWidgets.QComboBox(CommandFormWidget)
        self.comboBoxProvider.setEditable(True)
        self.comboBoxProvider.setObjectName("comboBoxProvider")
        self.verticalLayout_3.addWidget(self.comboBoxProvider)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(CommandFormWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(CommandFormWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.dateEditEmission = QtWidgets.QDateEdit(CommandFormWidget)
        self.dateEditEmission.setObjectName("dateEditEmission")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEditEmission)
        self.dateEditReception = QtWidgets.QDateEdit(CommandFormWidget)
        self.dateEditReception.setObjectName("dateEditReception")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEditReception)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(CommandFormWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAddArticle = QtWidgets.QPushButton(CommandFormWidget)
        self.pushButtonAddArticle.setObjectName("pushButtonAddArticle")
        self.horizontalLayout_2.addWidget(self.pushButtonAddArticle)
        self.pushButtonDeleteArticle = QtWidgets.QPushButton(CommandFormWidget)
        self.pushButtonDeleteArticle.setObjectName("pushButtonDeleteArticle")
        self.horizontalLayout_2.addWidget(self.pushButtonDeleteArticle)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(CommandFormWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.labelTotalCost = QtWidgets.QLabel(CommandFormWidget)
        self.labelTotalCost.setObjectName("labelTotalCost")
        self.horizontalLayout_2.addWidget(self.labelTotalCost)
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
        self.pushButtonAddArticle.setText(_translate("CommandFormWidget", "Ajouter un article"))
        self.pushButtonDeleteArticle.setText(_translate("CommandFormWidget", "Supprimer"))
        self.label_4.setText(_translate("CommandFormWidget", "Total :"))
        self.labelTotalCost.setText(_translate("CommandFormWidget", "0,0 F CFA"))

