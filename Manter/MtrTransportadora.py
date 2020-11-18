from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QTableView

import Banco
from UI import MtrTransportadora_ui

class MtrTransportadora(QDialog):
    def __init__(self):
        super(MtrTransportadora, self).__init__()

        self.op = ''

        self.ui = MtrTransportadora_ui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.txtId.setEnabled(False)
        self.ui.txtTransportadora.setEnabled(False)
        self.ui.txtCNPJ.setEnabled(False)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.habilitarJanelas(True)

        # Eventos
        self.ui.btnNovo.clicked.connect (self.clickedNovo)
        self.ui.btnAlterar.clicked.connect (self.clickedAlterar)
        self.ui.btnExcluir.clicked.connect (self.clickedExcluir)
        self.ui.btnSalvar.clicked.connect (self.clickedSalvar)
        self.ui.btnCancelar.clicked.connect (self.clickedCancelar)
        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.clicked.connect (self.clicked_table)

        self.carregarTable()
        self.ui.tableView.clicked.connect(self.clicked_table)


    def habilitarJanelas(self, ativo):
        # self.ui.txtId.setEnabled(not ativo)
        self.ui.txtTransportadora.setEnabled(not ativo)
        self.ui.txtCNPJ.setEnabled(not ativo)
        self.ui.btnNovo.setEnabled(ativo)
        self.ui.btnAlterar.setEnabled(ativo)
        self.ui.btnExcluir.setEnabled(ativo)
        self.ui.btnSalvar.setEnabled(not ativo)
        self.ui.btnCancelar.setEnabled(not ativo)

    def carregarTable(self):
        db = QSqlDatabase().addDatabase('QSQLITE')
        db.setDatabaseName('Litterarius.db')
        if db.open ():
            model = QSqlTableModel (self, db)
            model.setTable("transportadoras")
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.tableView.show ()

        db.close ()
        QSqlDatabase.removeDatabase('Litterarius.db')

    def clicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtTransportadora.setText (str (self.ui.tableView.model().data(index[1])))

    def limparJanelas(self):
        self.ui.txtId.setText ("")
        self.ui.txtTransportadora.setText ("")
        self.ui.txtCNPJ.setText ("")

    def clickedNovo(self):
        self.habilitarJanelas (False)
        self.limparJanelas ()
        self.ui.txtTransportadora.setFocus ()
        self.op = 'N'

    def clickedAlterar(self):
        valores = []
        self.habilitarJanelas (False)
        self.op = 'A'

        # txtEditora.setText(str(selection[0]))

    def clickedExcluir(self):
        Banco.excluirTransportadora (self.ui.txtId.text ())
        self.carregarTable ()

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirTransportadora (self.ui.txtTransportadora.text(), self.ui.txtCNPJ.text())
        elif self.op == 'A':
            Banco.alterarTransportadora (self.ui.txtId.text(),
                                         self.ui.txtTransportadora.text (),
                                         self.ui.txtCNPJ.text())
        self.habilitarJanelas(True)
        self.carregarTable()

    def clickedCancelar(self):
        self.habilitarJanelas (True)
