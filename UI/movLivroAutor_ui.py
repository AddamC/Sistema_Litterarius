# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movLivroAutor.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 317)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 471, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnIncluir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnIncluir.setObjectName("btnIncluir")
        self.verticalLayout.addWidget(self.btnIncluir)
        self.btnRetirar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnRetirar.setObjectName("btnRetirar")
        self.verticalLayout.addWidget(self.btnRetirar)
        self.gridLayout.addLayout(self.verticalLayout, 3, 2, 1, 1)
        self.lvAutor = QtWidgets.QListView(self.gridLayoutWidget)
        self.lvAutor.setObjectName("lvAutor")
        self.gridLayout.addWidget(self.lvAutor, 3, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.lwLivroAutor = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lwLivroAutor.setObjectName("lwLivroAutor")
        self.gridLayout.addWidget(self.lwLivroAutor, 3, 3, 2, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.lblAutores = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblAutores.setText("")
        self.lblAutores.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAutores.setObjectName("lblAutores")
        self.gridLayout.addWidget(self.lblAutores, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnIncluir.setText(_translate("Form", ">>"))
        self.btnRetirar.setText(_translate("Form", "<<"))
        self.label.setText(_translate("Form", "Autores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

