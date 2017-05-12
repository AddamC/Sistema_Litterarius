# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MtrEditora.ui'
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 631, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.txtEditora = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtEditora.setObjectName("txtEditora")
        self.gridLayout.addWidget(self.txtEditora, 3, 3, 1, 1)
        self.txtId = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtId.setObjectName("txtId")
        self.gridLayout.addWidget(self.txtId, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 6, 1, 1, 6)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 7, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnNovo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnNovo.setObjectName("btnNovo")
        self.verticalLayout.addWidget(self.btnNovo)
        self.btnAlterar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAlterar.setObjectName("btnAlterar")
        self.verticalLayout.addWidget(self.btnAlterar)
        self.btnExcluir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnExcluir.setObjectName("btnExcluir")
        self.verticalLayout.addWidget(self.btnExcluir)
        self.btnSalvar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSalvar.setObjectName("btnSalvar")
        self.verticalLayout.addWidget(self.btnSalvar)
        self.btnCancelar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        self.verticalLayout.addWidget(self.btnCancelar)
        self.gridLayout.addLayout(self.verticalLayout, 1, 5, 4, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "id"))
        self.label_2.setText(_translate("Form", "Descricao"))
        self.label_3.setText(_translate("Form", "Editoras"))
        self.btnNovo.setText(_translate("Form", "Novo"))
        self.btnAlterar.setText(_translate("Form", "Alterar"))
        self.btnExcluir.setText(_translate("Form", "Excluir"))
        self.btnSalvar.setText(_translate("Form", "Salvar"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

