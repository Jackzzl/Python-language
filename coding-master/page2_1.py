# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

class Ui_Page2_1(object):
    def setupUi(self, Page2_1):
        Page2_1.setObjectName("Page2_1")
        Page2_1.resize(400, 400)

        self.page = Page2_1
        self.page.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #1
        self.page.setFixedSize(Page2_1.width(), Page2_1.height()) #2窗口调整不可用

        self.verticalLayoutWidget = QtWidgets.QWidget(Page2_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 311, 295))
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
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
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

        self.retranslateUi(Page2_1)
        QtCore.QMetaObject.connectSlotsByName(Page2_1)

    def retranslateUi(self, Page2_1):
        _translate = QtCore.QCoreApplication.translate
        Page2_1.setWindowTitle(_translate("Page2_1", "Dialog"))
        self.label_10.setText(_translate("Page2_1", "请输入各符号概率："))
        self.label_2.setText(_translate("Page2_1", "香农编码"))
        self.label_8.setText(_translate("Page2_1", "a6:"))
        self.label_6.setText(_translate("Page2_1", "a4："))
        self.label_4.setText(_translate("Page2_1", "a2："))
        self.label.setText(_translate("Page2_1", "a1："))
        self.label_3.setText(_translate("Page2_1", "a3："))
        self.label_7.setText(_translate("Page2_1", "a5："))
        self.label_5.setText(_translate("Page2_1", "编码结果："))
        self.pushButton.setText(_translate("Page2_1", "确认"))
        self.pushButton_2.setText(_translate("Page2_1", "返回"))


        self.pushButton_2.clicked.connect(self.jumpToStart)
        self.pushButton.clicked.connect(self.Shannon)

    def jumpToStart(self):
        self.page.close()

    def Shannon(self):
        p = []
        result = ""
        s = 0.0
        p.append(float(self.lineEdit.text()))
        p.append(float(self.lineEdit_2.text()))
        p.append(float(self.lineEdit_3.text()))
        p.append(float(self.lineEdit_4.text()))
        p.append(float(self.lineEdit_5.text()))
        p.append(float(self.lineEdit_6.text()))
        p.sort(reverse=True)

        for i in range(0, 6):
            code = ""
            k = ceil(-log2(p[i]))  # 码长
            binary = s
            for j in range(0, k):
                if binary * 2 > 1:
                    binary = binary * 2
                    code = code + "1"
                    binary = binary - 1
                elif binary * 2 < 1:
                    binary = binary * 2
                    code = code + "0"
            result = result + code + " "
            s = s + p[i]

        self.label_5.setText("编码结果：" + result)
        print(result)
