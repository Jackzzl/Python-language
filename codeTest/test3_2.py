# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page3_2(object):
    def setupUi(self, Page3_2):
        Page3_2.setObjectName("Page3_2")
        Page3_2.resize(521, 308)

        self.page=Page3_2
        self.label_4 = QtWidgets.QLabel(Page3_2)
        self.label_4.setGeometry(QtCore.QRect(240, 160, 210, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Page3_2)
        self.lineEdit.setGeometry(QtCore.QRect(240, 120, 210, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Page3_2)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 51, 26))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Page3_2)
        self.label_3.setGeometry(QtCore.QRect(160, 170, 41, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Page3_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 240, 134, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Page3_2)
        self.pushButton.setGeometry(QtCore.QRect(340, 240, 131, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Page3_2)
        QtCore.QMetaObject.connectSlotsByName(Page3_2)

    def retranslateUi(self, Page3_2):
        _translate = QtCore.QCoreApplication.translate
        Page3_2.setWindowTitle(_translate("Page3_2", "Dialog"))
        self.label_2.setText(_translate("Page3_2", "请输入："))
        self.label_3.setText(_translate("Page3_2", "结果："))
        self.pushButton_2.setText(_translate("Page3_2", "确认"))
        self.pushButton.setText(_translate("Page3_2", "返回"))

        self.pushButton_2.clicked.connect(self.HUM)

    def HUM(self):
        code = bin(int(self.lineEdit.text()))
        code = str(code)[2:]
        #	判断待验证位数是否达到12位，不足位数前面补0
        while len(code) < 12:
            code = '0' + code
        code_list = list(code)
        code_1 = int(code_list[0]) ^ int(code_list[1]) ^ int(code_list[3]) ^ int(code_list[4]) ^ int(
            code_list[6]) ^ int(code_list[8]) ^ int(code_list[10]) ^ int(code_list[11])
        code_2 = int(code_list[0]) ^ int(code_list[2]) ^ int(code_list[3]) ^ int(code_list[5]) ^ int(
            code_list[6]) ^ int(code_list[9]) ^ int(code_list[10])
        code_4 = int(code_list[1]) ^ int(code_list[2]) ^ int(code_list[3]) ^ int(code_list[7]) ^ int(
            code_list[8]) ^ int(code_list[9]) ^ int(code_list[10])
        code_8 = int(code_list[4]) ^ int(code_list[5]) ^ int(code_list[6]) ^ int(code_list[7]) ^ int(
            code_list[8]) ^ int(code_list[9]) ^ int(code_list[10])
        code_16 = int(code_list[11])
        code_list.insert(0, str(code_1))
        code_list.insert(1, str(code_2))
        code_list.insert(3, str(code_4))
        code_list.insert(7, str(code_8))
        code_list.insert(15, str(code_16))
        result = ''.join(code_list)
        self.label_4.setText(result)


