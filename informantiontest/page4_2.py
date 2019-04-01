# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page4_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page4_2(object):
    def setupUi(self, Page4_2):
        Page4_2.setObjectName("Page4_2")
        Page4_2.resize(400, 400)

        self.page = Page4_2
        self.page.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #1
        self.page.setFixedSize(Page4_2.width(), Page4_2.height()) #2窗口调整不可用


        self.verticalLayoutWidget = QtWidgets.QWidget(Page4_2)
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

        self.retranslateUi(Page4_2)
        QtCore.QMetaObject.connectSlotsByName(Page4_2)

    def retranslateUi(self, Page4_2):
        _translate = QtCore.QCoreApplication.translate
        Page4_2.setWindowTitle(_translate("Page4_2", "Dialog"))
        self.label.setText(_translate("Page4_2", "LZ编码"))
        self.label_2.setText(_translate("Page4_2", "请输入(仅考虑abc)："))
        self.label_3.setText(_translate("Page4_2", "结果："))
        self.pushButton_2.setText(_translate("Page4_2", "确认"))
        self.pushButton.setText(_translate("Page4_2", "返回"))

        self.pushButton.clicked.connect(self.jumpToStart)
        self.pushButton_2.clicked.connect(self.LZ)

    def jumpToStart(self):
        self.page.close()

    def LZ(self):
        pass