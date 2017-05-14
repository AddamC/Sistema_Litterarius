# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Venda.ui'
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 631, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.btnContinuar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnContinuar.setObjectName("btnContinuar")
        self.gridLayout.addWidget(self.btnContinuar, 7, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.tbvCliente = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tbvCliente.setObjectName("tbvCliente")
        self.gridLayout.addWidget(self.tbvCliente, 4, 4, 1, 2)
        self.btnAddLivro = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddLivro.setObjectName("btnAddLivro")
        self.gridLayout.addWidget(self.btnAddLivro, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.btnBuscarCliente = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnBuscarCliente.setObjectName("btnBuscarCliente")
        self.gridLayout.addWidget(self.btnBuscarCliente, 3, 4, 1, 1)
        self.btnCadNovo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCadNovo.setObjectName("btnCadNovo")
        self.gridLayout.addWidget(self.btnCadNovo, 3, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 3, 1, 1)
        self.tbvCarrinho = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tbvCarrinho.setObjectName("tbvCarrinho")
        self.gridLayout.addWidget(self.tbvCarrinho, 4, 1, 1, 2)
        self.lblCliente = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblCliente.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lblCliente.setObjectName("lblCliente")
        self.gridLayout.addWidget(self.lblCliente, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "R$200,00"))
        self.btnContinuar.setText(_translate("Form", "Continuar"))
        self.label.setText(_translate("Form", "Carrinho:"))
        self.btnAddLivro.setText(_translate("Form", "Adicionar Livro"))
        self.label_4.setText(_translate("Form", "Cliente:"))
        self.label_2.setText(_translate("Form", "Preço Total:"))
        self.btnBuscarCliente.setText(_translate("Form", "Buscar Cliente"))
        self.btnCadNovo.setText(_translate("Form", "Cadastrar Novo"))
        self.lblCliente.setText(_translate("Form", "Maria Lucia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

