# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/article-list.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArticleListWidget(object):
    def setupUi(self, ArticleListWidget):
        ArticleListWidget.setObjectName("ArticleListWidget")
        ArticleListWidget.resize(828, 557)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ArticleListWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ArticleListWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(ArticleListWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEditSearchQuery = QtWidgets.QLineEdit(ArticleListWidget)
        self.lineEditSearchQuery.setObjectName("lineEditSearchQuery")
        self.horizontalLayout_2.addWidget(self.lineEditSearchQuery)
        self.pushButtonSearch = QtWidgets.QPushButton(ArticleListWidget)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.horizontalLayout_2.addWidget(self.pushButtonSearch)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView = QtWidgets.QTableView(ArticleListWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonUpdate = QtWidgets.QPushButton(ArticleListWidget)
        self.pushButtonUpdate.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout.addWidget(self.pushButtonUpdate)
        self.pushButtonDelete = QtWidgets.QPushButton(ArticleListWidget)
        self.pushButtonDelete.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(238, 238, 236);")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonInventaire = QtWidgets.QPushButton(ArticleListWidget)
        self.pushButtonInventaire.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.pushButtonInventaire.setObjectName("pushButtonInventaire")
        self.horizontalLayout.addWidget(self.pushButtonInventaire)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonQuit = QtWidgets.QPushButton(ArticleListWidget)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout.addWidget(self.pushButtonQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ArticleListWidget)
        QtCore.QMetaObject.connectSlotsByName(ArticleListWidget)

    def retranslateUi(self, ArticleListWidget):
        _translate = QtCore.QCoreApplication.translate
        ArticleListWidget.setWindowTitle(_translate("ArticleListWidget", "Stock | Aricles en stock"))
        self.label.setText(_translate("ArticleListWidget", "Liste de articles et leurs quantités en stock"))
        self.label_2.setText(_translate("ArticleListWidget", "Rechercher un article :"))
        self.pushButtonSearch.setText(_translate("ArticleListWidget", "Rechercher"))
        self.pushButtonUpdate.setText(_translate("ArticleListWidget", "Modifier"))
        self.pushButtonDelete.setText(_translate("ArticleListWidget", "Supprimer"))
        self.pushButtonInventaire.setText(_translate("ArticleListWidget", "Effectuer un inventaire"))
        self.pushButtonQuit.setText(_translate("ArticleListWidget", "Quitter"))

