

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import test1_1
import test1_2
import test2_1
import test2_2
import test2_3
import test3_1
import test3_2
import test4_1
import test4_2

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.mainwindow=MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(520, 110, 93, 28))
        self.Button1.setObjectName("Button1")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(340, 100, 141, 41))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(170, 100, 111, 31))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(170, 160, 91, 41))
        self.label2.setObjectName("label2")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(340, 160, 141, 41))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(520, 170, 93, 31))
        self.Button2.setObjectName("Button2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(170, 230, 91, 41))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(170, 310, 72, 31))
        self.label4.setObjectName("label4")
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(340, 230, 141, 41))
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(340, 300, 141, 41))
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(520, 240, 91, 28))
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(520, 310, 93, 28))
        self.Button4.setObjectName("Button4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "实验一选择"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "信道容量判定"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "唯一可译码判定"))
        self.label1.setText(_translate("MainWindow", "实验一"))
        self.label2.setText(_translate("MainWindow", "实验二"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "香农编码"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "霍夫曼编码"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "费诺编码"))
        self.Button2.setText(_translate("MainWindow", "实验二选择"))
        self.label3.setText(_translate("MainWindow", "实验三"))
        self.label4.setText(_translate("MainWindow", "实验四"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "LZW编码"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "Hamming"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "MH码"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "LZ编码"))
        self.Button3.setText(_translate("MainWindow", "实验三选择"))
        self.Button4.setText(_translate("MainWindow", "实验四选择"))

        self.Button1.clicked.connect(self.Test1)
        self.Button2.clicked.connect(self.Test2)
        self.Button3.clicked.connect(self.Test3)
        self.Button4.clicked.connect(self.Test4)


    def Test1(self):
        if self.comboBox1.currentText()=="信道容量判定":
            self.mainwindow.hide()
            dialog1_1 = QtWidgets.QDialog()
            ui = test1_1.Ui_Page1_1()
            ui.setupUi(dialog1_1)
            dialog1_1.show()
            dialog1_1.exec()
            self.mainwindow.show()

        elif self.comboBox1.currentText() == "唯一可译码判定":
            self.mainwindow.hide()
            dialog1_2 = QtWidgets.QDialog()
            ui = test1_2.Ui_Page1_2()
            ui.setupUi(dialog1_2)
            dialog1_2.show()
            dialog1_2.exec()
            self.mainwindow.show()

    def Test2(self):
        if  self.comboBox2.currentText()=="香农编码":
            self.mainwindow.hide()
            dialog2_1 = QtWidgets.QDialog()
            ui = test2_1.Ui_Page2_1()
            ui.setupUi(dialog2_1)
            dialog2_1.show()
            dialog2_1.exec()
            self.mainwindow.show()

        elif self.comboBox2.currentText()=="霍夫曼编码":
            self.mainwindow.hide()
            dialog2_2 = QtWidgets.QDialog()
            ui = test2_2.Ui_Page2_2()
            ui.setupUi(dialog2_2)
            dialog2_2.show()
            dialog2_2.exec()
            self.mainwindow.show()

        elif self.comboBox2.currentText()=="费诺编码":
            self.mainwindow.hide()
            dialog2_3 = QtWidgets.QDialog()
            ui = test2_3.Ui_Page2_3()
            ui.setupUi(dialog2_3)
            dialog2_3.show()
            dialog2_3.exec()
            self.mainwindow.show()

    def Test3(self):
        if  self.comboBox3.currentText()=="LZW编码":
            self.mainwindow.hide()
            dialog3_1 = QtWidgets.QDialog()
            ui = test3_1.Ui_Page3_1()
            ui.setupUi(dialog3_1)
            dialog3_1.show()
            dialog3_1.exec()
            self.mainwindow.show()

        elif self.comboBox3.currentText()=="Hamming":
            self.mainwindow.hide()
            dialog3_2 = QtWidgets.QDialog()
            ui = test3_2.Ui_Page3_2()
            ui.setupUi(dialog3_2)
            dialog3_2.show()
            dialog3_2.exec()
            self.mainwindow.show()

    def Test4(self):
        if  self.comboBox4.currentText()=="MH码":
            self.mainwindow.hide()
            dialog4_1 = QtWidgets.QDialog()
            ui = test4_1.Ui_Page4_1()
            ui.setupUi(dialog4_1)
            dialog4_1.show()
            dialog4_1.exec()
            self.mainwindow.show()

        elif self.comboBox4.currentText()=="LZ编码":
            self.mainwindow.hide()
            dialog4_2 = QtWidgets.QDialog()
            ui = test4_2.Ui_Page4_2()
            ui.setupUi(dialog4_2)
            dialog4_2.show()
            dialog4_2.exec()
            self.mainwindow.show()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    start = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    start.setupUi(w)
    w.show()
    sys.exit(app.exec_())