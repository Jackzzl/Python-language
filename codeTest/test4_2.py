# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page4_2(object):
    def setupUi(self, Page4_2):
        Page4_2.setObjectName("Page4_2")
        Page4_2.resize(660, 271)

        self.page=Page4_2
        self.label_2 = QtWidgets.QLabel(Page4_2)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 60, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Page4_2)
        self.label_3.setGeometry(QtCore.QRect(200, 120, 45, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Page4_2)
        self.label_4.setGeometry(QtCore.QRect(280, 120, 277, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Page4_2)
        self.lineEdit.setGeometry(QtCore.QRect(280, 60, 277, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Page4_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 190, 135, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Page4_2)
        self.pushButton.setGeometry(QtCore.QRect(400, 190, 141, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Page4_2)
        QtCore.QMetaObject.connectSlotsByName(Page4_2)

    def retranslateUi(self, Page4_2):
        _translate = QtCore.QCoreApplication.translate
        Page4_2.setWindowTitle(_translate("Page4_2", "Dialog"))
        self.label_2.setText(_translate("Page4_2", "请输入："))
        self.label_3.setText(_translate("Page4_2", "结果："))
        self.pushButton_2.setText(_translate("Page4_2", "确认"))
        self.pushButton.setText(_translate("Page4_2", "返回"))

        self.pushButton_2.clicked.connect(self.LZ)

    def LZ(self):
        def compress(message):
            tree_dict, m_len, i = {}, len(message), 0
            while i < m_len:
                # case I
                if message[i] not in tree_dict.keys():
                    yield (0, message[i])
                    tree_dict[message[i]] = len(tree_dict) + 1
                    i += 1
                # case III
                elif i == m_len - 1:
                    yield (tree_dict.get(message[i]), '')
                    i += 1
                else:
                    for j in range(i + 1, m_len):
                        # case II
                        if message[i:j + 1] not in tree_dict.keys():
                            yield (tree_dict.get(message[i:j]), message[j])
                            tree_dict[message[i:j + 1]] = len(tree_dict) + 1
                            i = j + 1
                            break
                        # case III
                        elif j == m_len - 1:
                            yield (tree_dict.get(message[i:j + 1]), '')
                            i = j + 1
            print(tree_dict)
            self.label_4.setText(str(tree_dict))

        def uncompress(packed):
            unpacked, tree_dict = '', {}
            for index, ch in packed:
                if index == 0:
                    unpacked += ch
                    tree_dict[len(tree_dict) + 1] = ch
                else:
                    term = tree_dict.get(index) + ch
                    unpacked += term
                    tree_dict[len(tree_dict) + 1] = term
            return unpacked

        s = self.lineEdit.text()
        pack = compress(s)
        unpack = uncompress(pack)


