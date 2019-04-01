# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

class Ui_Page1_1(object):
    def setupUi(self, Page1_1):
        Page1_1.setObjectName("Page1_1")
        Page1_1.resize(400, 400)

        self.page = Page1_1
        self.page.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #1
        self.page.setFixedSize(Page1_1.width(), Page1_1.height()) #2窗口调整不可用

        self.verticalLayoutWidget = QtWidgets.QWidget(Page1_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 337, 267))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 1, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 3, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 2, 4, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 0, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Page1_1)
        QtCore.QMetaObject.connectSlotsByName(Page1_1)

    def retranslateUi(self, Page1_1):
        _translate = QtCore.QCoreApplication.translate
        Page1_1.setWindowTitle(_translate("Page1_1", "Dialog"))
        self.label.setText(_translate("Page1_1", "对称DMC信道容量"))
        self.label_10.setText(_translate("Page1_1", "请输入信道转移概率矩阵："))
        self.label_7.setText(_translate("Page1_1", "　P="))
        self.label_2.setText(_translate("Page1_1", "信道容量为： 0 bit/符号"))
        self.pushButton.setText(_translate("Page1_1", "确定"))
        self.pushButton_2.setText(_translate("Page1_1", "返回"))

        self.pushButton_2.clicked.connect(self.jumpToStart)
        self.pushButton.clicked.connect(self.DMC)

    def jumpToStart(self):
        self.page.close()

    def DMC(self):
        a = []
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
            s = s + log2(i) * i
        s = s + log2(6)
        self.label_2.setText(("信道容量为：" + str(s) + "bit/符号"))

