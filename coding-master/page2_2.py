# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page2_2(object):
    def setupUi(self, Page2_2):
        Page2_2.setObjectName("Page2_2")
        Page2_2.resize(400, 400)

        self.page = Page2_2
        self.page.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #1
        self.page.setFixedSize(Page2_2.width(), Page2_2.height()) #2窗口调整不可用

        self.verticalLayoutWidget = QtWidgets.QWidget(Page2_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 311, 295))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Page2_2)
        QtCore.QMetaObject.connectSlotsByName(Page2_2)

    def retranslateUi(self, Page2_2):
        _translate = QtCore.QCoreApplication.translate
        Page2_2.setWindowTitle(_translate("Page2_2", "Dialog"))
        self.label_2.setText(_translate("Page2_2", "霍夫曼编码"))
        self.label_9.setText(_translate("Page2_2", "请输入各符号概率："))
        self.label_8.setText(_translate("Page2_2", "a6:"))
        self.label_6.setText(_translate("Page2_2", "a4："))
        self.label_4.setText(_translate("Page2_2", "a2："))
        self.label.setText(_translate("Page2_2", "a1："))
        self.label_3.setText(_translate("Page2_2", "a3："))
        self.label_7.setText(_translate("Page2_2", "a5："))
        self.label_5.setText(_translate("Page2_2", "编码结果："))
        self.pushButton.setText(_translate("Page2_2", "确认"))
        self.pushButton_2.setText(_translate("Page2_2", "返回"))

        self.pushButton_2.clicked.connect(self.jumpToStart)
        self.pushButton.clicked.connect(self.Huffman)

    def jumpToStart(self):
        self.page.close()

    def Huffman(self):
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

        self.label_5.setText("编码结果：" + result)
