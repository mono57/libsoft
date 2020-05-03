# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'article-command-list.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArticleCommandListWidget(object):
    def setupUi(self, ArticleCommandListWidget):
        ArticleCommandListWidget.setObjectName("ArticleCommandListWidget")
        ArticleCommandListWidget.resize(683, 400)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ArticleCommandListWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ArticleCommandListWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(ArticleCommandListWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(ArticleCommandListWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.labelTotalArticle = QtWidgets.QLabel(ArticleCommandListWidget)
        self.labelTotalArticle.setObjectName("labelTotalArticle")
        self.horizontalLayout.addWidget(self.labelTotalArticle)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonQuit = QtWidgets.QPushButton(ArticleCommandListWidget)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout.addWidget(self.pushButtonQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ArticleCommandListWidget)
        QtCore.QMetaObject.connectSlotsByName(ArticleCommandListWidget)

    def retranslateUi(self, ArticleCommandListWidget):
        _translate = QtCore.QCoreApplication.translate
        ArticleCommandListWidget.setWindowTitle(_translate("ArticleCommandListWidget", "Form"))
        self.label.setText(_translate("ArticleCommandListWidget", "Liste des articles commandés"))
        self.label_3.setText(_translate("ArticleCommandListWidget", "Nombre d\'articles commandés :"))
        self.labelTotalArticle.setText(_translate("ArticleCommandListWidget", "0"))
        self.pushButtonQuit.setText(_translate("ArticleCommandListWidget", "Quitter"))

