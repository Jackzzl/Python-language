# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2_3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page2_3(object):
    def setupUi(self, Page2_3):
        Page2_3.setObjectName("Page2_3")
        Page2_3.resize(726, 516)

        self.page = Page2_3
        self.label_2 = QtWidgets.QLabel(Page2_3)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Page2_3)
        self.label.setGeometry(QtCore.QRect(160, 70, 31, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Page2_3)
        self.label_4.setGeometry(QtCore.QRect(160, 100, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Page2_3)
        self.label_3.setGeometry(QtCore.QRect(160, 130, 31, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit.setGeometry(QtCore.QRect(200, 70, 131, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 100, 131, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 130, 131, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Page2_3)
        self.label_6.setGeometry(QtCore.QRect(160, 160, 31, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Page2_3)
        self.label_7.setGeometry(QtCore.QRect(160, 190, 31, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Page2_3)
        self.label_8.setGeometry(QtCore.QRect(160, 220, 24, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 160, 131, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 190, 131, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 220, 131, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(Page2_3)
        self.label_5.setGeometry(QtCore.QRect(100, 300, 521, 41))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Page2_3)
        self.pushButton.setGeometry(QtCore.QRect(350, 470, 150, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Page2_3)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 470, 161, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(Page2_3)
        self.label_9.setGeometry(QtCore.QRect(160, 250, 31, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(Page2_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 250, 131, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Page2_3)
        QtCore.QMetaObject.connectSlotsByName(Page2_3)

    def retranslateUi(self, Page2_3):
        _translate = QtCore.QCoreApplication.translate
        Page2_3.setWindowTitle(_translate("Page2_3", "Dialog"))
        self.label_2.setText(_translate("Page2_3", "费诺编码"))
        self.label.setText(_translate("Page2_3", "a1："))
        self.label_4.setText(_translate("Page2_3", "a2："))
        self.label_3.setText(_translate("Page2_3", "a3："))
        self.label_6.setText(_translate("Page2_3", "a4："))
        self.label_7.setText(_translate("Page2_3", "a5："))
        self.label_8.setText(_translate("Page2_3", "a6:"))
        self.label_5.setText(_translate("Page2_3", "编码结果："))
        self.pushButton.setText(_translate("Page2_3", "确认"))
        self.pushButton_2.setText(_translate("Page2_3", "返回"))
        self.label_9.setText(_translate("Page2_3", "a7:"))

        self.pushButton.clicked.connect(self.FN)
        #self.pushButton_2.clicked.connect(self.ToStart)

    def FN(self):
        class Node:
            def __init__(self, freq):
                self.code = ''
                self.freq = freq  # 概率

        a = [0.20, 0.19, 0.18, 0.17, 0.15, 0.1]  # 排序
        nodes = []
        for i in range(0, 6):
            nodes.append(Node(a[i]))

        # 第一步
        p = 0
        q = 0
        s = 0
        for i in range(0, 6):
            if s < 0.5:
                s = s + nodes[i].freq
                record = i
            else:
                record = i
                p = s / 2  # 下一步的判断概率
                q = (1 - p) / 2  # 下一步的判断概率
                break
        # record=3
        for i in range(0, record):
            nodes[i].code = nodes[i].code + "1"
        for i in range(record, 6):
            nodes[i].code = nodes[i].code + "0"

        # 第二步
        # record=3
        # p=0.285
        # q=0.215
        for i in range(0, record):  # 0/1/2
            s = 0
            if s < p:
                s = s + nodes[i].freq
                r = i
            else:
                r = i  # r=1
                break
        # r
        for i in range(0, r):  # 0
            nodes[i].code = nodes[i].code + "1"
        for i in range(r, record):  # 1/2
            nodes[i].code = nodes[i].code + "0"

        # record=3
        # q=0.215
        for i in range(record, 6):  # 3/4/5
            s = 0
            if s < q:
                s = s + nodes[i].freq
                temp = i
            else:
                temp = i  # temp=4
                break
        # temp
        for i in range(record, temp):  # 3
            nodes[i].code = nodes[i].code + "1"
        for i in range(temp, 6):  # 4/5
            nodes[i].code = nodes[i].code + "0"

        self.label_5.setText("编码结果：00 010 011 10 110 111")
    """
    def fun():
        Q = x  # 通过队列进行处理
        while len(Q) > 1:
            Q.sort(key=lambda xx: xx.prob)  # 根据使用频度排序
            # for i in Q:
            #     print i.prob
            l = Q.pop(0)
            r = Q.pop(0)
            if l.name is not None:
                newQ.append(l)
            if r.name is not None:
                newQ.append(r)
            # 左1右0左小右大
            l.codeword = '0'
            r.codeword = '1'

            fa = hafnode(prob=l.prob + r.prob)
            fa.l = l
            fa.r = r
            l.fa = fa
            r.fa = fa
            Q.append(fa)

        Q[0].fa = None
        return Q[0]

    def hufdeal():
        root = fun()
        pro = []
        codes = [''] * len(newQ)
        symbol = []

        for i in range(len(newQ)):
            tmp = newQ[i]
            while tmp.fa != None:
                codes[i] = tmp.codeword + codes[i]
                tmp = tmp.fa
            newQ[i].codeword = codes[i]

    class hafnode():
        def __init__(self, name=None, prob=None, codeword='', procode=None):
            self.name = name
            self.prob = prob
            self.codeword = codeword
            self.procode = procode
            self.fa = None
            self.l = None
            self.codeword = None
        """



