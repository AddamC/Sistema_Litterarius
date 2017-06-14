# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movFornTransp.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 637, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.lvTransportadora = QtWidgets.QListView(self.gridLayoutWidget)
        self.lvTransportadora.setObjectName("lvTransportadora")
        self.gridLayout.addWidget(self.lvTransportadora, 3, 3, 2, 1)
        self.lvFornTransp = QtWidgets.QListView(self.gridLayoutWidget)
        self.lvFornTransp.setObjectName("lvFornTransp")
        self.gridLayout.addWidget(self.lvFornTransp, 3, 1, 2, 1)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.btnFornecedor = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.btnFornecedor.setObjectName("btnFornecedor")
        self.horizontalLayout_2.addWidget(self.btnFornecedor)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnIncluir.setText(_translate("Form", ">>"))
        self.btnRetirar.setText(_translate("Form", "<<"))
        self.label.setText(_translate("Form", "Forncedor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

