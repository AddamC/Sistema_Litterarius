# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pagamento.ui'
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.cbParcela = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbParcela.setObjectName("cbParcela")
        self.gridLayout.addWidget(self.cbParcela, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.txtPrecoCompra = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPrecoCompra.setObjectName("txtPrecoCompra")
        self.gridLayout.addWidget(self.txtPrecoCompra, 2, 2, 1, 1)
        self.txtCompraId = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtCompraId.setObjectName("txtCompraId")
        self.gridLayout.addWidget(self.txtCompraId, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 4, 1, 1)
        self.txtVlrParcela = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtVlrParcela.setObjectName("txtVlrParcela")
        self.gridLayout.addWidget(self.txtVlrParcela, 2, 5, 1, 1)
        self.cbxPago = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cbxPago.setObjectName("cbxPago")
        self.gridLayout.addWidget(self.cbxPago, 3, 5, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 5, 1, 1, 5)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.txtDataCompra = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtDataCompra.setObjectName("txtDataCompra")
        self.gridLayout.addWidget(self.txtDataCompra, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 6, 1, 1, 1)
        self.lblDataPago = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.lblDataPago.setFont(font)
        self.lblDataPago.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblDataPago.setObjectName("lblDataPago")
        self.gridLayout.addWidget(self.lblDataPago, 4, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.btnVoltar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnVoltar.setObjectName("btnVoltar")
        self.gridLayout.addWidget(self.btnVoltar, 6, 4, 1, 1)
        self.btnConfirmar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.gridLayout.addWidget(self.btnConfirmar, 6, 5, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Parcela"))
        self.label_6.setText(_translate("Form", "Está pago?"))
        self.txtVlrParcela.setText(_translate("Form", "TextLabel"))
        self.cbxPago.setText(_translate("Form", "CheckBox"))
        self.label_5.setText(_translate("Form", "Valor"))
        self.label.setText(_translate("Form", "Compra"))
        self.label_2.setText(_translate("Form", "Preço total da compra"))
        self.label_3.setText(_translate("Form", "Data da compra realizada"))
        self.label_8.setText(_translate("Form", "Pagamento"))
        self.lblDataPago.setText(_translate("Form", "TextLabel"))
        self.btnVoltar.setText(_translate("Form", "Voltar"))
        self.btnConfirmar.setText(_translate("Form", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
