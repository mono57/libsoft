# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/add-command-article-form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddCommandArticleWidget(object):
    def setupUi(self, AddCommandArticleWidget):
        AddCommandArticleWidget.setObjectName("AddCommandArticleWidget")
        AddCommandArticleWidget.resize(364, 119)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddCommandArticleWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(AddCommandArticleWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBoxArticle = QtWidgets.QComboBox(AddCommandArticleWidget)
        self.comboBoxArticle.setEnabled(True)
        self.comboBoxArticle.setEditable(False)
        self.comboBoxArticle.setObjectName("comboBoxArticle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxArticle)
        self.label_2 = QtWidgets.QLabel(AddCommandArticleWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBoxQteCommand = QtWidgets.QSpinBox(AddCommandArticleWidget)
        self.spinBoxQteCommand.setMinimum(1)
        self.spinBoxQteCommand.setObjectName("spinBoxQteCommand")
        self.horizontalLayout.addWidget(self.spinBoxQteCommand)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButtonAddArticle = QtWidgets.QPushButton(AddCommandArticleWidget)
        self.pushButtonAddArticle.setObjectName("pushButtonAddArticle")
        self.verticalLayout.addWidget(self.pushButtonAddArticle)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AddCommandArticleWidget)
        QtCore.QMetaObject.connectSlotsByName(AddCommandArticleWidget)

    def retranslateUi(self, AddCommandArticleWidget):
        _translate = QtCore.QCoreApplication.translate
        AddCommandArticleWidget.setWindowTitle(_translate("AddCommandArticleWidget", "Ajouter un article"))
        self.label.setText(_translate("AddCommandArticleWidget", "Article à commander : "))
        self.label_2.setText(_translate("AddCommandArticleWidget", "Quantité à commander : "))
        self.pushButtonAddArticle.setText(_translate("AddCommandArticleWidget", "Ajouter"))

