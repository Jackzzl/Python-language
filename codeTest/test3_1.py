# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page3_1(object):
    def setupUi(self, Page3_1):
        Page3_1.setObjectName("Page3_1")
        Page3_1.resize(598, 244)

        self.page=Page3_1
        self.pushButton_2 = QtWidgets.QPushButton(Page3_1)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 200, 135, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Page3_1)
        self.pushButton.setGeometry(QtCore.QRect(310, 200, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Page3_1)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 60, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Page3_1)
        self.lineEdit.setGeometry(QtCore.QRect(220, 100, 225, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Page3_1)
        self.label_3.setGeometry(QtCore.QRect(120, 140, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Page3_1)
        self.label_4.setGeometry(QtCore.QRect(221, 150, 221, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Page3_1)
        QtCore.QMetaObject.connectSlotsByName(Page3_1)

    def retranslateUi(self, Page3_1):
        _translate = QtCore.QCoreApplication.translate
        Page3_1.setWindowTitle(_translate("Page3_1", "Dialog"))
        self.pushButton_2.setText(_translate("Page3_1", "确认"))
        self.pushButton.setText(_translate("Page3_1", "返回"))
        self.label_2.setText(_translate("Page3_1", "请输入："))
        self.label_3.setText(_translate("Page3_1", "结果："))

        self.pushButton_2.clicked.connect(self.LZW)

    def LZW(self):
        string = "thisisthe"
        dictionary = {chr(i): i for i in range(97, 123)}

        last = 256
        p = ""
        final = ""
        result = []

        for c in string:
            pc = p + c
            if pc in dictionary:
                p = pc
            else:
                result.append(dictionary[p])
                dictionary[pc] = last
                last += 1
                p = c
        if p != '':
            result.append(dictionary[p])
        """
        for i in range(0,7):
            final = final + result[i]+" "
        """
        print(result)
        self.label_4.setText(final)


