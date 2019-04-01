# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

class Ui_Page2_1(object):
    def setupUi(self, Page2_1):
        Page2_1.setObjectName("Page2_1")
        Page2_1.resize(684, 413)

        self.page = Page2_1
        self.label_2 = QtWidgets.QLabel(Page2_1)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 160, 58))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Page2_1)
        self.label.setGeometry(QtCore.QRect(160, 90, 31, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Page2_1)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 112, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Page2_1)
        self.label_4.setGeometry(QtCore.QRect(160, 120, 31, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Page2_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 120, 112, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Page2_1)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 31, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Page2_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 150, 111, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Page2_1)
        self.label_6.setGeometry(QtCore.QRect(160, 180, 31, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Page2_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 180, 111, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(Page2_1)
        self.label_7.setGeometry(QtCore.QRect(160, 210, 31, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Page2_1)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 210, 111, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(Page2_1)
        self.label_8.setGeometry(QtCore.QRect(160, 240, 24, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(Page2_1)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 240, 111, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(Page2_1)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 370, 150, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Page2_1)
        self.pushButton.setGeometry(QtCore.QRect(300, 370, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Page2_1)
        self.label_5.setGeometry(QtCore.QRect(90, 310, 511, 31))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(Page2_1)
        self.label_11.setGeometry(QtCore.QRect(390, 90, 81, 16))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Page2_1)
        self.label_12.setGeometry(QtCore.QRect(390, 120, 72, 15))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Page2_1)
        self.label_13.setGeometry(QtCore.QRect(380, 150, 72, 15))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Page2_1)
        self.label_14.setGeometry(QtCore.QRect(380, 180, 72, 15))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Page2_1)
        self.label_15.setGeometry(QtCore.QRect(380, 190, 72, 15))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Page2_1)
        self.label_16.setGeometry(QtCore.QRect(390, 210, 72, 15))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Page2_1)
        self.label_17.setGeometry(QtCore.QRect(380, 240, 72, 15))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Page2_1)
        QtCore.QMetaObject.connectSlotsByName(Page2_1)

    def retranslateUi(self, Page2_1):
        _translate = QtCore.QCoreApplication.translate
        Page2_1.setWindowTitle(_translate("Page2_1", "Dialog"))
        self.label_2.setText(_translate("Page2_1", "香农编码"))
        self.label.setText(_translate("Page2_1", "a1："))
        self.label_4.setText(_translate("Page2_1", "a2："))
        self.label_3.setText(_translate("Page2_1", "a3："))
        self.label_6.setText(_translate("Page2_1", "a4："))
        self.label_7.setText(_translate("Page2_1", "a5："))
        self.label_8.setText(_translate("Page2_1", "a6:"))
        self.pushButton_2.setText(_translate("Page2_1", "返回"))
        self.pushButton.setText(_translate("Page2_1", "确认"))
        self.label_5.setText(_translate("Page2_1", "编码结果："))

        self.pushButton.clicked.connect(self.XN)
        #self.pushButton_2.clicked.connect(self.ToStart)

    def XN(self):
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
            """
            if j == 1:
                p.append(int(self.label_11.setText(result)))
            """
            s = s + p[i]

        self.label_5.setText("编码结果：a1 a2 a3 a4 a5 a6:" + result)
        print(result)

