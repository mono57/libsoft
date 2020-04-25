# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'article-search.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArticleSearchForm(object):
    def setupUi(self, ArticleSearchForm):
        ArticleSearchForm.setObjectName("ArticleSearchForm")
        ArticleSearchForm.resize(417, 58)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ArticleSearchForm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(ArticleSearchForm)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(ArticleSearchForm)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ArticleSearchForm)
        QtCore.QMetaObject.connectSlotsByName(ArticleSearchForm)

    def retranslateUi(self, ArticleSearchForm):
        _translate = QtCore.QCoreApplication.translate
        ArticleSearchForm.setWindowTitle(_translate("ArticleSearchForm", "Rechercher"))
        self.lineEdit.setPlaceholderText(_translate("ArticleSearchForm", "Entrez la recherche"))
        self.pushButton.setText(_translate("ArticleSearchForm", "Rechercher"))

