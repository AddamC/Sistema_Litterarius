from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QMdiSubWindow, QTableView

import Banco
import MtrAutor_ui

# TODO: Refatorar essa classe. Está com valores do MtrAutor
class MtrCliente(QDialog):
    def __init__(self):
        super(MtrCliente, self).__init__()
        self.ui = MtrCliente_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled (False)
        self.ui.txtAutor.setEnabled (False)

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
        self.ui.txtAutor.setEnabled(not ativo)

    def limparJanelas(self):
        self.ui.txtId.setText("")
        self.ui.txtAutor.setText("")

    def clickedNovo(self):
        self.habilitarJanelas(False)
        self.limparJanelas()
        self.ui.txtAutor.setFocus()
        self.op = 'N'

    def clickedAlterar(self):
        valores=[]
        self.habilitarJanelas(False)
        op = 'A'

        # txtAutor.setText(str(selection[0]))

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirCliente(self.ui.txtCliente.text()) # Passar parametros corretos de clientes
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
            model.setTable ("clientes")
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

        db.close()

    def carregarDados(self):
        cliente = Banco.selectClienteById(1)

        self.ui.txtId.setText(str(autor[0]))
        self.ui.txtAutor.setText(str(autor[1]))

    def doubleClicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtAutor.setText (str (self.ui.tableView.model().data(index[1])))