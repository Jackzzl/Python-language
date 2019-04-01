# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

class Ui_Page1_1(object):
    def setupUi(self, Page1_1):
        Page1_1.setObjectName("Page1_1")
        Page1_1.resize(580, 400)

        self.page = Page1_1
        self.label = QtWidgets.QLabel(Page1_1)
        self.label.setGeometry(QtCore.QRect(130, 40, 300, 40))
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Page1_1)
        self.widget.setGeometry(QtCore.QRect(150, 140, 335, 88))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 1, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 3, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 2, 4, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 0, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Page1_1)
        self.label_2.setGeometry(QtCore.QRect(360, 260, 176, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Page1_1)
        self.pushButton.setGeometry(QtCore.QRect(150, 350, 163, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Page1_1)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 350, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Page1_1)
        self.label_7.setGeometry(QtCore.QRect(60, 160, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit1 = QtWidgets.QTextEdit(Page1_1)
        self.textEdit1.setGeometry(QtCore.QRect(60, 240, 104, 87))
        self.textEdit1.setObjectName("textEdit1")

        self.retranslateUi(Page1_1)
        QtCore.QMetaObject.connectSlotsByName(Page1_1)

    def retranslateUi(self, Page1_1):
        _translate = QtCore.QCoreApplication.translate
        Page1_1.setWindowTitle(_translate("Page1_1", "Dialog"))
        self.label.setText(_translate("Page1_1", "对称DMC信道容量"))
        self.label_2.setText(_translate("Page1_1", "信道容量为： 0 bit/符号"))
        self.pushButton.setText(_translate("Page1_1", "确定"))
        self.pushButton_2.setText(_translate("Page1_1", "返回"))
        self.label_7.setText(_translate("Page1_1", "　P="))

        self.pushButton.clicked.connect(self.DMC)
        #self.pushButton_2.click.connect(self.ToStart)

    def ToStart(self):
        self.page.close()

    def DMC(self):
        a=[]
        #b=[[]*3]*3
        s = 0
        a.append(float(self.lineEdit_11.text()))
        a.append(float(self.lineEdit.text()))
        a.append(float(self.lineEdit_9.text()))
        a.append(float(self.lineEdit_10.text()))
        a.append(float(self.lineEdit_6.text()))
        a.append(float(self.lineEdit_7.text()))
        a.append(float(self.lineEdit_12.text()))
        a.append(float(self.lineEdit_5.text()))
        a.append(float(self.lineEdit_4.text()))
        a.append(float(self.lineEdit_3.text()))
        a.append(float(self.lineEdit_2.text()))
        a.append(float(self.lineEdit_8.text()))

        for i in a:
            s = s +log2(i) * i
        s = s + log2(64)
        self.label_2.setText(("信道容量为：" + str(s) + "bit/符号"))

