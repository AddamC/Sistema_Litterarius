# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MtrFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 631, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnNovo = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnNovo.setObjectName("btnNovo")
        self.verticalLayout_6.addWidget(self.btnNovo)
        self.btnAlterar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnAlterar.setObjectName("btnAlterar")
        self.verticalLayout_6.addWidget(self.btnAlterar)
        self.btnExcluir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnExcluir.setObjectName("btnExcluir")
        self.verticalLayout_6.addWidget(self.btnExcluir)
        self.btnSalvar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnSalvar.setObjectName("btnSalvar")
        self.verticalLayout_6.addWidget(self.btnSalvar)
        self.btnCancelar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnCancelar.setObjectName("btnCancelar")
        self.verticalLayout_6.addWidget(self.btnCancelar)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 4, 5, 2, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.txtNome = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtNome.setObjectName("txtNome")
        self.verticalLayout_7.addWidget(self.txtNome)
        self.txtCpf = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtCpf.setObjectName("txtCpf")
        self.verticalLayout_7.addWidget(self.txtCpf)
        self.txtTelefone = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtTelefone.setObjectName("txtTelefone")
        self.verticalLayout_7.addWidget(self.txtTelefone)
        self.txtRg = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtRg.setObjectName("txtRg")
        self.verticalLayout_7.addWidget(self.txtRg)
        self.txtEndereco = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtEndereco.setObjectName("txtEndereco")
        self.verticalLayout_7.addWidget(self.txtEndereco)
        self.txtSalario = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtSalario.setObjectName("txtSalario")
        self.verticalLayout_7.addWidget(self.txtSalario)
        self.txtTurno = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtTurno.setObjectName("txtTurno")
        self.verticalLayout_7.addWidget(self.txtTurno)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 6, 3, 1, 1)
        self.txtId = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtId.setObjectName("txtId")
        self.gridLayout_3.addWidget(self.txtId, 2, 3, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 7, 1, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 4, 6, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 3, 1, 3, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 4, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnNovo.setText(_translate("Form", "Novo"))
        self.btnAlterar.setText(_translate("Form", "Alterar"))
        self.btnExcluir.setText(_translate("Form", "Excluir"))
        self.btnSalvar.setText(_translate("Form", "Salvar"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))
        self.label_17.setText(_translate("Form", "Funcionários"))
        self.label_11.setText(_translate("Form", "NOME"))
        self.label_12.setText(_translate("Form", "CPF"))
        self.label_13.setText(_translate("Form", "TELEFONE"))
        self.label_14.setText(_translate("Form", "RG"))
        self.label_15.setText(_translate("Form", "ENDERECO"))
        self.label.setText(_translate("Form", "SALÁRIO"))
        self.label_2.setText(_translate("Form", "TURNO"))
        self.label_16.setText(_translate("Form", "id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

