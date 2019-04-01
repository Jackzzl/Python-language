# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page4_1(object):
    def setupUi(self, Page4_1):
        Page4_1.setObjectName("Page4_1")
        Page4_1.resize(554, 219)

        self.page=Page4_1
        self.label_2 = QtWidgets.QLabel(Page4_1)
        self.label_2.setGeometry(QtCore.QRect(170, 40, 60, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Page4_1)
        self.lineEdit.setGeometry(QtCore.QRect(290, 40, 225, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Page4_1)
        self.label_4.setGeometry(QtCore.QRect(290, 80, 221, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Page4_1)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 71, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Page4_1)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 140, 135, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Page4_1)
        self.pushButton.setGeometry(QtCore.QRect(310, 140, 131, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Page4_1)
        QtCore.QMetaObject.connectSlotsByName(Page4_1)

    def retranslateUi(self, Page4_1):
        _translate = QtCore.QCoreApplication.translate
        Page4_1.setWindowTitle(_translate("Page4_1", "Dialog"))
        self.label_2.setText(_translate("Page4_1", "请输入："))
        self.label_3.setText(_translate("Page4_1", "结果："))
        self.pushButton_2.setText(_translate("Page4_1", "确认"))
        self.pushButton.setText(_translate("Page4_1", "返回"))

        self.pushButton_2.clicked.connect(self.MH)

    def MH(self):
        s = self.lineEdit.text()
        result = ''
        last = s[0]
        count = 1
        for _ in s[1:]:
            if last == _:
                count += 1
            else:
                result += str(count) + last
                last = _
                count = 1
        result += str(count) + last
        self.label_4.setText(result)

