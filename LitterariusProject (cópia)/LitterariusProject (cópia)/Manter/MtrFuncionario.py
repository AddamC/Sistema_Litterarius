from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QTableView

import Banco
from UI import MtrFuncionario_ui


class MtrFuncionario(QDialog):
    def __init__(self):
        super(MtrFuncionario, self).__init__()
        self.ui = MtrFuncionario_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled (False)
        self.ui.txtNome.setEnabled (False)
        self.ui.txtCpf.setEnabled (False)
        self.ui.txtEndereco.setEnabled (False)
        self.ui.txtRg.setEnabled (False)
        self.ui.txtSalario.setEnabled (False)
        self.ui.txtTelefone.setEnabled (False)
        self.ui.txtTurno.setEnabled (False)

        self.carregarTable ()
        self.carregarDados ()

        self.habilitarJanelas (True)

        # Eventos
        self.ui.btnNovo.clicked.connect (self.clickedNovo)
        self.ui.btnAlterar.clicked.connect (self.clickedAlterar)
        self.ui.btnSalvar.clicked.connect (self.clickedSalvar)
        self.ui.btnCancelar.clicked.connect (self.clickedCancelar)
        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.doubleClicked.connect (self.doubleClicked_table)


    def habilitarJanelas(self, ativo):
        self.ui.btnNovo.setEnabled(ativo)
        self.ui.btnAlterar.setEnabled(ativo)
        self.ui.btnCancelar.setEnabled(not ativo)
        self.ui.btnExcluir.setEnabled(not ativo)
        self.ui.btnSalvar.setEnabled(not ativo)
        # txtId.setEnabled(not ativo)
        self.ui.txtNome.setEnabled(not ativo)
        self.ui.txtTurno.setEnabled (not ativo)
        self.ui.txtSalario.setEnabled (not ativo)
        self.ui.txtTelefone.setEnabled (not ativo)
        self.ui.txtEndereco.setEnabled (not ativo)
        self.ui.txtRg.setEnabled (not ativo)
        self.ui.txtCpf.setEnabled (not ativo)

    def limparJanelas(self):
        self.ui.txtId.setText("")
        self.ui.txtNome.setText("")
        self.ui.txtEndereco.setText ("")
        self.ui.txtCpf.setText ("")
        self.ui.txtRg.setText ("")
        self.ui.txtTelefone.setText ("")
        self.ui.txtSalario.setTxt ("")
        self.ui.txtTurno.setTxt ("")

    def clickedNovo(self):
        self.habilitarJanelas(False)
        self.limparJanelas()
        self.ui.txtNome.setFocus()
        self.op = 'N'

    def clickedAlterar(self):
        valores=[]
        self.habilitarJanelas(False)
        op = 'A'

        # txtAutor.setText(str(selection[0]))

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirAutor(self.ui.txtAutor.text())
        self.habilitarJanelas(True)
        self.carregarTable()

    def clickedCancelar(self):
        self.habilitarJanelas(True)


    def carregarTable(self):
        db = QSqlDatabase().addDatabase('QSQLITE')
        db.setDatabaseName('Litterarius.db')
        conexao = db.connectionName()
        if db.open():
            model = QSqlTableModel (self, db)
            model.setTable ("funcionarios")
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

        db.close()

    def carregarDados(self):
        autor = Banco.selectFuncionarioById(1)

        self.ui.txtId.setText(str(autor[0]))
        self.ui.txtNome.setText(str(autor[1]))
        # self.ui.txtCNPJ.setText (str (autor[2]))

    def doubleClicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        # self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        # self.ui.txtFornecedor.setText (str (self.ui.tableView.model().data(index[1])))
        # self.ui.txtCNPJ.setText (str (self.ui.tableView.model().data(index[2])))