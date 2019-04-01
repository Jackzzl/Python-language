# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Page1_2(object):
    def setupUi(self, page1_2):
        page1_2.setObjectName("page1_2")
        page1_2.resize(609, 400)

        self.page = page1_2
        self.label_2 = QtWidgets.QLabel(page1_2)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 320, 49))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(page1_2)
        self.pushButton.setGeometry(QtCore.QRect(180, 350, 176, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(page1_2)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 350, 191, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(page1_2)
        self.label.setGeometry(QtCore.QRect(130, 90, 31, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(page1_2)
        self.lineEdit.setGeometry(QtCore.QRect(190, 90, 296, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(page1_2)
        self.label_4.setGeometry(QtCore.QRect(130, 130, 21, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(page1_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 130, 296, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(page1_2)
        self.label_3.setGeometry(QtCore.QRect(130, 170, 31, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(page1_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 170, 301, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(page1_2)
        self.label_5.setGeometry(QtCore.QRect(130, 210, 31, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(page1_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 210, 301, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(page1_2)
        self.label_6.setGeometry(QtCore.QRect(210, 270, 151, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(page1_2)
        QtCore.QMetaObject.connectSlotsByName(page1_2)

    def retranslateUi(self, page1_2):
        _translate = QtCore.QCoreApplication.translate
        page1_2.setWindowTitle(_translate("page1_2", "Dialog"))
        self.label_2.setText(_translate("page1_2", "唯一可译码的判断"))
        self.pushButton.setText(_translate("page1_2", "确认"))
        self.pushButton_2.setText(_translate("page1_2", "返回"))
        self.label.setText(_translate("page1_2", "a1："))
        self.label_4.setText(_translate("page1_2", "a2："))
        self.label_3.setText(_translate("page1_2", "a3："))
        self.label_5.setText(_translate("page1_2", "a4:"))

        #self.puchButton_2.clicked.connect(self.ToStart)
        self.pushButton.clicked.connect(self.UDC)

    def ToStart(self):
            self.page.close()

    def UDC(self):
            a1 = self.lineEdit.text()
            a2 = self.lineEdit_2.text()
            a3 = self.lineEdit_3.text()
            a4 = self.lineEdit_4.text()
            code1=len(a1)
            code2=len(a2)
            code3=len(a3)
            code4=len(a4)

            judge= 2**-code1+ 2**-code2+ 2**-code3+ 2**-code4

            if code1 ==code2 or code1==code3 or code1 ==code4 or code2==code3 or code2==code4 or code3==code4:
                self.label_6.setText("不是唯一可译码")

            elif judge >1 :
                self.label_6.setText("是唯一可译码")

            elif judge <=1:
                self.label_6.setText("不是唯一可译码")

