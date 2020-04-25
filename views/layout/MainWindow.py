# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_article = QtWidgets.QPushButton(self.groupBox_3)
        self.add_article.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_article.setAutoFillBackground(False)
        self.add_article.setCheckable(False)
        self.add_article.setFlat(False)
        self.add_article.setObjectName("add_article")
        self.verticalLayout_2.addWidget(self.add_article)
        self.search_article = QtWidgets.QPushButton(self.groupBox_3)
        self.search_article.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_article.setFlat(False)
        self.search_article.setObjectName("search_article")
        self.verticalLayout_2.addWidget(self.search_article)
        self.add_history = QtWidgets.QPushButton(self.groupBox_3)
        self.add_history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("history")
        self.add_history.setIcon(icon)
        self.add_history.setFlat(False)
        self.add_history.setObjectName("add_history")
        self.verticalLayout_2.addWidget(self.add_history)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_command = QtWidgets.QPushButton(self.groupBox)
        self.add_command.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_command.setFlat(False)
        self.add_command.setObjectName("add_command")
        self.verticalLayout_3.addWidget(self.add_command)
        self.command_history = QtWidgets.QPushButton(self.groupBox)
        self.command_history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.command_history.setFlat(False)
        self.command_history.setObjectName("command_history")
        self.verticalLayout_3.addWidget(self.command_history)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_selling = QtWidgets.QPushButton(self.groupBox_2)
        self.add_selling.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_selling.setFlat(False)
        self.add_selling.setObjectName("add_selling")
        self.verticalLayout_4.addWidget(self.add_selling)
        self.selling_history = QtWidgets.QPushButton(self.groupBox_2)
        self.selling_history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selling_history.setFlat(False)
        self.selling_history.setObjectName("selling_history")
        self.verticalLayout_4.addWidget(self.selling_history)
        self.selling_rapport = QtWidgets.QPushButton(self.groupBox_2)
        self.selling_rapport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selling_rapport.setFlat(False)
        self.selling_rapport.setObjectName("selling_rapport")
        self.verticalLayout_4.addWidget(self.selling_rapport)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_2.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Articles"))
        self.add_article.setText(_translate("MainWindow", "Ajouter un article"))
        self.search_article.setText(_translate("MainWindow", "Rechercher un article"))
        self.add_history.setText(_translate("MainWindow", "Historique des ajouts"))
        self.groupBox.setTitle(_translate("MainWindow", "Commandes"))
        self.add_command.setText(_translate("MainWindow", "Enregistrer une commande"))
        self.command_history.setText(_translate("MainWindow", "Historique des commandes"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ventes"))
        self.add_selling.setText(_translate("MainWindow", "Enregistrer une vente"))
        self.selling_history.setText(_translate("MainWindow", "Historique des ventes"))
        self.selling_rapport.setText(_translate("MainWindow", "Rapport des ventes"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
