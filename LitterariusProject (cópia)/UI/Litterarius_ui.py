# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LitterariusUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(928, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnSair = QtWidgets.QPushButton(Dialog)
        self.btnSair.setObjectName("btnSair")
        self.gridLayout_2.addWidget(self.btnSair, 2, 3, 1, 1)
        self.btnManter = QtWidgets.QPushButton(Dialog)
        self.btnManter.setObjectName("btnManter")
        self.gridLayout_2.addWidget(self.btnManter, 2, 1, 1, 1)
        self.btnRelat = QtWidgets.QPushButton(Dialog)
        self.btnRelat.setObjectName("btnRelat")
        self.gridLayout_2.addWidget(self.btnRelat, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        self.btnMovimentar = QtWidgets.QPushButton(Dialog)
        self.btnMovimentar.setObjectName("btnMovimentar")
        self.gridLayout_2.addWidget(self.btnMovimentar, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.mdiArea = QtWidgets.QMdiArea(Dialog)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_3.addWidget(self.mdiArea, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSair.setText(_translate("Dialog", "Sair"))
        self.btnManter.setText(_translate("Dialog", "Manter"))
        self.btnRelat.setText(_translate("Dialog", "Relatorios"))
        self.label.setText(_translate("Dialog", "Litterarius"))
        self.btnMovimentar.setText(_translate("Dialog", "Movimentar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

