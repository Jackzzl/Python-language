# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page3_2(object):
    def setupUi(self, Page3_2):
        Page3_2.setObjectName("Page3_2")
        Page3_2.resize(400, 400)

        self.page = Page3_2
        self.page.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 1
        self.page.setFixedSize(Page3_2.width(), Page3_2.height())  # 2窗口调整不可用

        self.verticalLayoutWidget = QtWidgets.QWidget(Page3_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 80, 281, 221))
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
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Page3_2)
        QtCore.QMetaObject.connectSlotsByName(Page3_2)

    def retranslateUi(self, Page3_2):
        _translate = QtCore.QCoreApplication.translate
        Page3_2.setWindowTitle(_translate("Page3_2", "Dialog"))
        self.label.setText(_translate("Page3_2", "Hamming编码"))
        self.label_2.setText(_translate("Page3_2", "请输入："))
        self.label_3.setText(_translate("Page3_2", "结果："))
        self.pushButton_2.setText(_translate("Page3_2", "确认"))
        self.pushButton.setText(_translate("Page3_2", "返回"))

        self.pushButton.clicked.connect(self.jumpToStart)
        self.pushButton_2.clicked.connect(self.Hamming)

    def jumpToStart(self):
        self.page.close()

    def Hamming(self):
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
