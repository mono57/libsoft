# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/inventaire.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InventaireWidget(object):
    def setupUi(self, InventaireWidget):
        InventaireWidget.setObjectName("InventaireWidget")
        InventaireWidget.resize(350, 170)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(InventaireWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(InventaireWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(InventaireWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.checkBox = QtWidgets.QCheckBox(InventaireWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(InventaireWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(InventaireWidget)
        self.comboBox.setEditable(True)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(InventaireWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(InventaireWidget)
        QtCore.QMetaObject.connectSlotsByName(InventaireWidget)

    def retranslateUi(self, InventaireWidget):
        _translate = QtCore.QCoreApplication.translate
        InventaireWidget.setWindowTitle(_translate("InventaireWidget", "Form"))
        self.label.setText(_translate("InventaireWidget", "Inventaire d\'articles"))
        self.label_2.setText(_translate("InventaireWidget", "Tous les articles "))
        self.label_3.setText(_translate("InventaireWidget", "Sectionner l\'article"))
        self.pushButton.setText(_translate("InventaireWidget", "Faire l\'inventaire"))

