from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QTableView, QAbstractItemView

import Banco
from UI import MtrAutor_ui


# TODO: Update, Delete, Cancel
class MtrAutor(QDialog):
    def __init__(self):
        super(MtrAutor, self).__init__()
        self.ui = MtrAutor_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled (False)
        self.ui.txtAutor.setEnabled (False)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.carregarTable ()
        self.carregarDados ()

        self.habilitarJanelas (True)

        # Eventos
        self.ui.btnNovo.clicked.connect (self.clickedNovo)
        self.ui.btnAlterar.clicked.connect (self.clickedAlterar)
        self.ui.btnSalvar.clicked.connect (self.clickedSalvar)
        self.ui.btnCancelar.clicked.connect (self.clickedCancelar)
        self.ui.btnExcluir.clicked.connect(self.clickedExcluir)
        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.clicked.connect (self.doubleClicked_table)


    def habilitarJanelas(self, ativo):
        self.ui.btnNovo.setEnabled(ativo)
        self.ui.btnAlterar.setEnabled(ativo)
        self.ui.btnCancelar.setEnabled(not ativo)
        self.ui.btnExcluir.setEnabled(ativo)
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
        self.op = 'A'

    def clickedExcluir(self):
        Banco.excluirAutor (self.ui.txtId.text ())
        self.habilitarJanelas (True)
        self.carregarTable ()
        # txtAutor.setText(str(selection[0]))

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirAutor(self.ui.txtAutor.text())
        elif self.op == 'A':
            Banco.alterarAutor(self.ui.txtId.text(), self.ui.txtAutor.text())
        self.habilitarJanelas(True)
        self.carregarTable()

    def clickedCancelar(self):
        self.habilitarJanelas(True)


    def carregarTable(self):
        db = QSqlDatabase().addDatabase('QSQLITE')
        db.setDatabaseName('Litterarius.db')
        if db.open():
            model = QSqlTableModel (self, db)
            model.setTable ("autores")
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()
        db.close()
        QSqlDatabase().removeDatabase('Litterarius.db')

    def carregarDados(self):
        autor = Banco.selectAutorById(1)

        self.ui.txtId.setText(str(autor))
        self.ui.txtAutor.setText(str(autor))

    def doubleClicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtAutor.setText (str (self.ui.tableView.model().data(index[1])))