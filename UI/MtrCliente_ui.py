# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MtrCliente.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(640, 480)
        Form.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 641, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 1, 3, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txtNome = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNome.setObjectName("txtNome")
        self.verticalLayout_4.addWidget(self.txtNome)
        self.txtCpf = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtCpf.setObjectName("txtCpf")
        self.verticalLayout_4.addWidget(self.txtCpf)
        self.txtTelefone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtTelefone.setObjectName("txtTelefone")
        self.verticalLayout_4.addWidget(self.txtTelefone)
        self.txtRg = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtRg.setObjectName("txtRg")
        self.verticalLayout_4.addWidget(self.txtRg)
        self.txtEndereco = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtEndereco.setObjectName("txtEndereco")
        self.verticalLayout_4.addWidget(self.txtEndereco)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 3, 3, 3, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 6, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnNovo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnNovo.setObjectName("btnNovo")
        self.verticalLayout_2.addWidget(self.btnNovo)
        self.btnAlterar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAlterar.setObjectName("btnAlterar")
        self.verticalLayout_2.addWidget(self.btnAlterar)
        self.btnExcluir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnExcluir.setObjectName("btnExcluir")
        self.verticalLayout_2.addWidget(self.btnExcluir)
        self.btnSalvar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSalvar.setObjectName("btnSalvar")
        self.verticalLayout_2.addWidget(self.btnSalvar)
        self.btnCancelar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        self.verticalLayout_2.addWidget(self.btnCancelar)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 3, 5, 3, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 8, 1, 1, 6)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 7, 4, 1, 1)
        self.txtId = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtId.setObjectName("txtId")
        self.gridLayout_2.addWidget(self.txtId, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "NOME"))
        self.label_7.setText(_translate("Form", "CPF"))
        self.label_9.setText(_translate("Form", "TELEFONE"))
        self.label_4.setText(_translate("Form", "RG"))
        self.label_10.setText(_translate("Form", "ENDERECO"))
        self.label_5.setText(_translate("Form", "id"))
        self.btnNovo.setText(_translate("Form", "Novo"))
        self.btnAlterar.setText(_translate("Form", "Alterar"))
        self.btnExcluir.setText(_translate("Form", "Excluir"))
        self.btnSalvar.setText(_translate("Form", "Salvar"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))
        self.label_6.setText(_translate("Form", "Clientes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
