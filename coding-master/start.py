# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codingUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import page1_1
import page1_2
import page2_1
import page2_2
import page2_3
import page3_1
import page3_2
import page4_1
import page4_2
import sys

class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.mainwindow = MainWindow
        self.mainwindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #禁止最大化按钮
        self.mainwindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 391, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.helloLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(18)
        self.helloLabel.setFont(font)
        self.helloLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.helloLabel.setTextFormat(QtCore.Qt.AutoText)
        self.helloLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.helloLabel.setObjectName("helloLabel")
        self.verticalLayout.addWidget(self.helloLabel)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.gridLayout.addWidget(self.comboBox2, 1, 1, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 4, 0, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 2, 0, 1, 1)
        self.comboBox3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.gridLayout.addWidget(self.comboBox3, 2, 1, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 0, 0, 1, 1)
        self.comboBox4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.gridLayout.addWidget(self.comboBox4, 4, 1, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.helloLabel.setBuddy(self.helloLabel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helloLabel.setText(_translate("MainWindow", "请选择相应内容并点击内容前的按钮开始实验"))

        self.button1.setText(_translate("MainWindow", "基础理论"))
        self.comboBox.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox.setItemText(1, _translate("MainWindow", "信道容量"))
        self.comboBox.setItemText(2, _translate("MainWindow", "唯一可译码"))

        self.button2.setText(_translate("MainWindow", "信源编码方式"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "香农编码"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "霍夫曼编码"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "费诺编码"))

        self.button3.setText(_translate("MainWindow", "编码仿真"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "LZW编码"))
        self.comboBox3.setItemText(2, _translate("MainWindow", "Hamming(7,4)编译码器"))

        self.button4.setText(_translate("MainWindow", "综合"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "MH码"))
        self.comboBox4.setItemText(2, _translate("MainWindow", "LZ码"))

        self.button1.clicked.connect(self.jumpToPage1)
        self.button2.clicked.connect(self.jumpToPage2)
        self.button3.clicked.connect(self.jumpToPage3)
        self.button4.clicked.connect(self.jumpToPage4)


    def msg(self):
        QMessageBox.about(self, "提示", "请选择具体实验")

    def jumpToPage1(self):
        if self.comboBox.currentText() == "请选择":
            self.msg()
            return

        elif self.comboBox.currentText() == "唯一可译码":
            self.mainwindow.hide()
            dialog1_2 = QtWidgets.QDialog()
            ui = page1_2.Ui_Page1_2()
            ui.setupUi(dialog1_2)
            dialog1_2.show()
            dialog1_2.exec()
            self.mainwindow.show()

        elif self.comboBox.currentText() == "信道容量":
            self.mainwindow.hide()
            dialog1_1 = QtWidgets.QDialog()
            ui = page1_1.Ui_Page1_1()
            ui.setupUi(dialog1_1)
            dialog1_1.show()
            dialog1_1.exec()
            self.mainwindow.show()

    def jumpToPage2(self):
        if self.comboBox2.currentText() == "请选择":
            self.msg()
            return

        elif self.comboBox2.currentText() == "香农编码":
            self.mainwindow.hide()
            dialog2_1 = QtWidgets.QDialog()
            ui = page2_1.Ui_Page2_1()
            ui.setupUi(dialog2_1)
            dialog2_1.show()
            dialog2_1.exec()
            self.mainwindow.show()

        elif self.comboBox2.currentText() == "霍夫曼编码":
            self.mainwindow.hide()
            dialog2_2 = QtWidgets.QDialog()
            ui = page2_2.Ui_Page2_2()
            ui.setupUi(dialog2_2)
            dialog2_2.show()
            dialog2_2.exec()
            self.mainwindow.show()

        elif self.comboBox2.currentText() == "费诺编码":
            self.mainwindow.hide()
            dialog2_3 = QtWidgets.QDialog()
            ui = page2_3.Ui_Page2_3()
            ui.setupUi(dialog2_3)
            dialog2_3.show()
            dialog2_3.exec()
            self.mainwindow.show()


    def jumpToPage3(self):
        if self.comboBox3.currentText() == "请选择":
            self.msg()
            return

        elif self.comboBox3.currentText() == "LZW编码":
            self.mainwindow.hide()
            dialog3_1 = QtWidgets.QDialog()
            ui = page3_1.Ui_Page3_1()
            ui.setupUi(dialog3_1)
            dialog3_1.show()
            dialog3_1.exec()
            self.mainwindow.show()

        elif self.comboBox3.currentText() == "Hamming(7,4)编译码器":
            self.mainwindow.hide()
            dialog3_2 = QtWidgets.QDialog()
            ui = page3_2.Ui_Page3_2()
            ui.setupUi(dialog3_2)
            dialog3_2.show()
            dialog3_2.exec()
            self.mainwindow.show()

    def jumpToPage4(self):
        if self.comboBox4.currentText() == "请选择":
            self.msg()
            return

        elif self.comboBox4.currentText() == "游程编码":
            self.mainwindow.hide()
            dialog4_1 = QtWidgets.QDialog()
            ui = page4_1.Ui_Page4_1()
            ui.setupUi(dialog4_1)
            dialog4_1.show()
            dialog4_1.exec()
            self.mainwindow.show()


        elif self.comboBox4.currentText() == "LZ码":
            self.mainwindow.hide()
            dialog4_2 = QtWidgets.QDialog()
            ui = page4_2.Ui_Page4_2()
            ui.setupUi(dialog4_2)
            dialog4_2.show()
            dialog4_2.exec()
            self.mainwindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    start.setupUi(w)
    w.show()
    sys.exit(app.exec_())
