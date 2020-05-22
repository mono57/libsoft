# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/article-form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArticleForm(object):
    def setupUi(self, ArticleForm):
        ArticleForm.setObjectName("ArticleForm")
        ArticleForm.resize(506, 373)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ArticleForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(-1, 0, -1, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ArticleForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEditCode = QtWidgets.QLineEdit(ArticleForm)
        self.lineEditCode.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"padding: 2px;")
        self.lineEditCode.setObjectName("lineEditCode")
        self.verticalLayout_5.addWidget(self.lineEditCode)
        self.labelErrorCode = QtWidgets.QLabel(ArticleForm)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelErrorCode.setFont(font)
        self.labelErrorCode.setStyleSheet("color: rgb(239, 41, 41)")
        self.labelErrorCode.setText("")
        self.labelErrorCode.setObjectName("labelErrorCode")
        self.verticalLayout_5.addWidget(self.labelErrorCode)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_5)
        self.label_3 = QtWidgets.QLabel(ArticleForm)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEditDesignation = QtWidgets.QLineEdit(ArticleForm)
        self.lineEditDesignation.setObjectName("lineEditDesignation")
        self.verticalLayout_6.addWidget(self.lineEditDesignation)
        self.labelErrorDesignation = QtWidgets.QLabel(ArticleForm)
        self.labelErrorDesignation.setText("")
        self.labelErrorDesignation.setObjectName("labelErrorDesignation")
        self.verticalLayout_6.addWidget(self.labelErrorDesignation)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_6)
        self.label_2 = QtWidgets.QLabel(ArticleForm)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBoxFamilly = QtWidgets.QComboBox(ArticleForm)
        self.comboBoxFamilly.setToolTipDuration(-1)
        self.comboBoxFamilly.setEditable(True)
        self.comboBoxFamilly.setObjectName("comboBoxFamilly")
        self.comboBoxFamilly.addItem("")
        self.comboBoxFamilly.addItem("")
        self.comboBoxFamilly.addItem("")
        self.comboBoxFamilly.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxFamilly)
        self.label_4 = QtWidgets.QLabel(ArticleForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_10 = QtWidgets.QLabel(ArticleForm)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_5 = QtWidgets.QLabel(ArticleForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEditBuyPrice = QtWidgets.QLineEdit(ArticleForm)
        self.lineEditBuyPrice.setObjectName("lineEditBuyPrice")
        self.verticalLayout_7.addWidget(self.lineEditBuyPrice)
        self.labelErrorBuyingPrice = QtWidgets.QLabel(ArticleForm)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelErrorBuyingPrice.setFont(font)
        self.labelErrorBuyingPrice.setStyleSheet("color: red;")
        self.labelErrorBuyingPrice.setText("")
        self.labelErrorBuyingPrice.setObjectName("labelErrorBuyingPrice")
        self.verticalLayout_7.addWidget(self.labelErrorBuyingPrice)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(ArticleForm)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(ArticleForm)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEditSellingPrice = QtWidgets.QLineEdit(ArticleForm)
        self.lineEditSellingPrice.setObjectName("lineEditSellingPrice")
        self.verticalLayout_8.addWidget(self.lineEditSellingPrice)
        self.labelErrorSellingPrice = QtWidgets.QLabel(ArticleForm)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelErrorSellingPrice.setFont(font)
        self.labelErrorSellingPrice.setStyleSheet("color: red;\n"
"")
        self.labelErrorSellingPrice.setText("")
        self.labelErrorSellingPrice.setObjectName("labelErrorSellingPrice")
        self.verticalLayout_8.addWidget(self.labelErrorSellingPrice)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(ArticleForm)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_7 = QtWidgets.QLabel(ArticleForm)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBoxQteStock = QtWidgets.QSpinBox(ArticleForm)
        self.spinBoxQteStock.setEnabled(False)
        self.spinBoxQteStock.setObjectName("spinBoxQteStock")
        self.horizontalLayout_4.addWidget(self.spinBoxQteStock)
        self.labelErrorQuantity = QtWidgets.QLabel(ArticleForm)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelErrorQuantity.setFont(font)
        self.labelErrorQuantity.setStyleSheet("color: red")
        self.labelErrorQuantity.setText("")
        self.labelErrorQuantity.setObjectName("labelErrorQuantity")
        self.horizontalLayout_4.addWidget(self.labelErrorQuantity)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.comboBoxEditor = QtWidgets.QComboBox(ArticleForm)
        self.comboBoxEditor.setEditable(True)
        self.comboBoxEditor.setObjectName("comboBoxEditor")
        self.comboBoxEditor.addItem("")
        self.comboBoxEditor.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxEditor)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEditAuthor = QtWidgets.QLineEdit(ArticleForm)
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.horizontalLayout_5.addWidget(self.lineEditAuthor)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonSave = QtWidgets.QPushButton(ArticleForm)
        self.pushButtonSave.setEnabled(True)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonSaveAndQuit = QtWidgets.QPushButton(ArticleForm)
        self.pushButtonSaveAndQuit.setEnabled(True)
        self.pushButtonSaveAndQuit.setObjectName("pushButtonSaveAndQuit")
        self.horizontalLayout.addWidget(self.pushButtonSaveAndQuit)
        self.pushButtonQuit = QtWidgets.QPushButton(ArticleForm)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout.addWidget(self.pushButtonQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ArticleForm)
        self.comboBoxFamilly.setCurrentIndex(0)
        self.comboBoxEditor.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ArticleForm)

    def retranslateUi(self, ArticleForm):
        _translate = QtCore.QCoreApplication.translate
        ArticleForm.setWindowTitle(_translate("ArticleForm", "Ajout d\'un article"))
        self.label.setText(_translate("ArticleForm", "Code :"))
        self.lineEditCode.setInputMask(_translate("ArticleForm", "AAA99AA"))
        self.lineEditCode.setPlaceholderText(_translate("ArticleForm", "AAA99AA"))
        self.label_3.setText(_translate("ArticleForm", "Designation :"))
        self.label_2.setText(_translate("ArticleForm", "Famille :"))
        self.comboBoxFamilly.setCurrentText(_translate("ArticleForm", "Cassete"))
        self.comboBoxFamilly.setItemText(0, _translate("ArticleForm", "Cassete"))
        self.comboBoxFamilly.setItemText(1, _translate("ArticleForm", "Divers sujets bibliques"))
        self.comboBoxFamilly.setItemText(2, _translate("ArticleForm", "Affiches"))
        self.comboBoxFamilly.setItemText(3, _translate("ArticleForm", "Bible"))
        self.label_4.setText(_translate("ArticleForm", "Auteur :"))
        self.label_10.setText(_translate("ArticleForm", "Editeur :"))
        self.label_5.setText(_translate("ArticleForm", "Prix d\'achat :"))
        self.label_8.setText(_translate("ArticleForm", "F CFA"))
        self.label_6.setText(_translate("ArticleForm", "Prix de vente :"))
        self.label_9.setText(_translate("ArticleForm", "F CFA"))
        self.label_7.setText(_translate("ArticleForm", "Quantité stock :"))
        self.comboBoxEditor.setItemText(0, _translate("ArticleForm", "BMP"))
        self.comboBoxEditor.setItemText(1, _translate("ArticleForm", "Nouvel élément"))
        self.pushButtonSave.setText(_translate("ArticleForm", "Enregistrer"))
        self.pushButtonSaveAndQuit.setText(_translate("ArticleForm", "Enregistrer et quitter"))
        self.pushButtonQuit.setText(_translate("ArticleForm", "Quitter"))

