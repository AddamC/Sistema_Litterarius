# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MtrLivro.ui'
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 621, 461))
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
        self.gridLayout_3.addLayout(self.verticalLayout_6, 3, 5, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 3, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 6, 1, 1, 5)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 3, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.txtId = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtId.setObjectName("txtId")
        self.gridLayout_2.addWidget(self.txtId, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.lblISBN = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblISBN.setObjectName("lblISBN")
        self.gridLayout_2.addWidget(self.lblISBN, 4, 0, 1, 1)
        self.txtISBN = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtISBN.setObjectName("txtISBN")
        self.gridLayout_2.addWidget(self.txtISBN, 4, 1, 1, 1)
        self.txtQTDE = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtQTDE.setObjectName("txtQTDE")
        self.gridLayout_2.addWidget(self.txtQTDE, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.txtValor = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtValor.setObjectName("txtValor")
        self.gridLayout_2.addWidget(self.txtValor, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 6, 1, 1)
        self.tbGenero = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.tbGenero.setObjectName("tbGenero")
        self.gridLayout_2.addWidget(self.tbGenero, 2, 7, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 6, 1, 1)
        self.tbAutor = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.tbAutor.setObjectName("tbAutor")
        self.gridLayout_2.addWidget(self.tbAutor, 3, 7, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 6, 1, 1)
        self.cbEditora = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.cbEditora.setObjectName("cbEditora")
        self.gridLayout_2.addWidget(self.cbEditora, 4, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 6, 1, 1)
        self.ckbConsignado = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.ckbConsignado.setText("")
        self.ckbConsignado.setObjectName("ckbConsignado")
        self.gridLayout_2.addWidget(self.ckbConsignado, 5, 7, 1, 1)
        self.txtTitulo = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtTitulo.setObjectName("txtTitulo")
        self.gridLayout_2.addWidget(self.txtTitulo, 3, 1, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 1, 2, 3)

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
        self.label_17.setText(_translate("Form", "Livros"))
        self.label_16.setText(_translate("Form", "id"))
        self.label_11.setText(_translate("Form", "TÍTULO"))
        self.lblISBN.setText(_translate("Form", "ISBN"))
        self.label.setText(_translate("Form", "QTDE"))
        self.label_2.setText(_translate("Form", "VALOR UNITÁRIO"))
        self.label_15.setText(_translate("Form", "GÊNERO"))
        self.tbGenero.setText(_translate("Form", "..."))
        self.label_14.setText(_translate("Form", "AUTOR"))
        self.tbAutor.setText(_translate("Form", "..."))
        self.label_13.setText(_translate("Form", "EDITORA"))
        self.label_3.setText(_translate("Form", "CONSIGNADO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
