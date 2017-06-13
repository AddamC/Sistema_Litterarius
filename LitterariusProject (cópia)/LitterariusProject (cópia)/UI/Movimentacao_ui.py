# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Movimentacao.ui'
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 641, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnPagamento = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnPagamento.setObjectName("btnPagamento")
        self.gridLayout.addWidget(self.btnPagamento, 1, 0, 1, 1)
        self.btnDetCompra = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDetCompra.setObjectName("btnDetCompra")
        self.gridLayout.addWidget(self.btnDetCompra, 0, 0, 1, 1)
        self.btnDetVenda = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDetVenda.setObjectName("btnDetVenda")
        self.gridLayout.addWidget(self.btnDetVenda, 0, 1, 1, 1)
        self.btnRecebimento = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnRecebimento.setObjectName("btnRecebimento")
        self.gridLayout.addWidget(self.btnRecebimento, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnPagamento.setText(_translate("Form", "Pagamento"))
        self.btnDetCompra.setText(_translate("Form", "Detalhe compra"))
        self.btnDetVenda.setText(_translate("Form", "Detalhe venda"))
        self.btnRecebimento.setText(_translate("Form", "Recebimento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

