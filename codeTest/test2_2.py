# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page2_2(object):
    def setupUi(self, Page2_2):
        Page2_2.setObjectName("Page2_2")
        Page2_2.resize(648, 400)

        self.page=Page2_2
        self.label_2 = QtWidgets.QLabel(Page2_2)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 200, 42))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Page2_2)
        self.label.setGeometry(QtCore.QRect(170, 60, 31, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Page2_2)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 112, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Page2_2)
        self.label_4.setGeometry(QtCore.QRect(170, 90, 31, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Page2_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 90, 112, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Page2_2)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 31, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Page2_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 120, 111, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Page2_2)
        self.label_6.setGeometry(QtCore.QRect(170, 150, 31, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Page2_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 150, 111, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(Page2_2)
        self.label_7.setGeometry(QtCore.QRect(170, 180, 31, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Page2_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 180, 111, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(Page2_2)
        self.label_8.setGeometry(QtCore.QRect(170, 210, 24, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(Page2_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 210, 111, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(Page2_2)
        self.label_5.setGeometry(QtCore.QRect(100, 270, 471, 41))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Page2_2)
        self.pushButton.setGeometry(QtCore.QRect(250, 360, 150, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Page2_2)
        self.pushButton_2.setGeometry(QtCore.QRect(416, 360, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Page2_2)
        QtCore.QMetaObject.connectSlotsByName(Page2_2)

    def retranslateUi(self, Page2_2):
        _translate = QtCore.QCoreApplication.translate
        Page2_2.setWindowTitle(_translate("Page2_2", "Dialog"))
        self.label_2.setText(_translate("Page2_2", "霍夫曼编码"))
        self.label.setText(_translate("Page2_2", "a1："))
        self.label_4.setText(_translate("Page2_2", "a2："))
        self.label_3.setText(_translate("Page2_2", "a3："))
        self.label_6.setText(_translate("Page2_2", "a4："))
        self.label_7.setText(_translate("Page2_2", "a5："))
        self.label_8.setText(_translate("Page2_2", "a6:"))
        self.label_5.setText(_translate("Page2_2", "编码结果："))
        self.pushButton.setText(_translate("Page2_2", "确认"))
        self.pushButton_2.setText(_translate("Page2_2", "返回"))

        self.pushButton.clicked.connect(self.Huf)
        #self.pushButton_2.clicked.connect(self.ToStart)


    def Huf(self):
        # Tree-Node Type
        class Node:
            def __init__(self, freq):
                self.left = None  # 左节点
                self.right = None  # 右节点
                self.father = None  # 父节点
                self.freq = freq  # 概率

            def isLeft(self):
                return self.father.left == self

        # create nodes创建叶子节点
        def createNodes(freqs):
            return [Node(freq) for freq in freqs]

        # create Huffman-Tree创建Huffman树
        def createHuffmanTree(nodes):
            queue = nodes[:]
            while len(queue) > 1:
                queue.sort(key=lambda item: item.freq)
                node_left = queue.pop(0)
                node_right = queue.pop(0)
                node_father = Node(node_left.freq + node_right.freq)
                node_father.left = node_left
                node_father.right = node_right
                node_left.father = node_father
                node_right.father = node_father
                queue.append(node_father)
            queue[0].father = None
            return queue[0]

        # Huffman编码
        def huffmanEncoding(nodes, root):
            codes = [''] * len(nodes)
            for i in range(len(nodes)):
                node_tmp = nodes[i]
                while node_tmp != root:
                    if node_tmp.isLeft():
                        codes[i] = '0' + codes[i]
                    else:
                        codes[i] = '1' + codes[i]
                    node_tmp = node_tmp.father
            return codes

        p = []
        result = ""
        p.append(float(self.lineEdit.text()))
        p.append(float(self.lineEdit_2.text()))
        p.append(float(self.lineEdit_3.text()))
        p.append(float(self.lineEdit_4.text()))
        p.append(float(self.lineEdit_5.text()))
        p.append(float(self.lineEdit_6.text()))
        p.sort(reverse=True)
        nodes = createNodes([item for item in p])
        root = createHuffmanTree(nodes)
        codes = huffmanEncoding(nodes, root)
        for i in range(0, 6):
            result = result + codes[i] + " "

        #self.label_5.setText("编码结果：" + result)
        self.label_5.setText("编码结果：a1 a2 a3 a4 a5 a6 " + result)


