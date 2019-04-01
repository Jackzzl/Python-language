# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Page1_2(object):
    def setupUi(self, page1_2):
        page1_2.setObjectName("page1_2")
        page1_2.resize(400, 400)

        self.page = page1_2
        self.page.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #1
        self.page.setFixedSize(page1_2.width(), page1_2.height()) #2窗口调整不可用

        self.verticalLayoutWidget = QtWidgets.QWidget(page1_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 311, 270))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(page1_2)
        QtCore.QMetaObject.connectSlotsByName(page1_2)

    def retranslateUi(self, page1_2):
        _translate = QtCore.QCoreApplication.translate
        page1_2.setWindowTitle(_translate("page1_2", "Dialog"))
        self.label_2.setText(_translate("page1_2", "唯一可译码的判断"))
        self.label.setText(_translate("page1_2", "code1："))
        self.label_4.setText(_translate("page1_2", "code2："))
        self.label_3.setText(_translate("page1_2", "code3："))
        self.label_5.setText(_translate("page1_2", "是否存在唯一可译码：待确定"))
        self.pushButton.setText(_translate("page1_2", "确认"))
        self.pushButton_2.setText(_translate("page1_2", "返回"))

        self.pushButton_2.clicked.connect(self.jumpToStart)
        self.pushButton.clicked.connect(self.UDC)

    def jumpToStart(self):
        self.page.close()

    def UDC(self):
        code1 = self.lineEdit.text()
        code2 = self.lineEdit_2.text()
        code3 = self.lineEdit_3.text()
        codeLen1 = len(code1)
        codeLen2 = len(code2)
        codeLen3 = len(code3)

        kraft = 2 ** -codeLen1 + 2 ** -codeLen2 + 2 ** -codeLen3

        if code1 == code2 or code2 == code3 or code1 == code3:
            self.label_5.setText("是否存在唯一可译码：否")

        elif kraft > 1:
            self.label_5.setText("是否存在唯一可译码：是")

        elif kraft <= 1:
            self.label_5.setText("是否存在唯一可译码：否")










