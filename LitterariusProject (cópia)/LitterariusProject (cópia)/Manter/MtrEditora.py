from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QTableView, QAbstractItemView

import Banco
from UI import MtrEditora_ui


class MtrEditora(QDialog):
    def __init__(self):
        super(MtrEditora, self).__init__()
        self.ui = MtrEditora_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled (False)
        self.ui.txtEditora.setEnabled (False)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.carregarTable ()
        self.carregarDados ()

        self.habilitarJanelas (True)

        # Eventos
        self.ui.btnNovo.clicked.connect (self.clickedNovo)
        self.ui.btnAlterar.clicked.connect (self.clickedAlterar)
        self.ui.btnExcluir.clicked.connect (self.clickedExcluir)
        self.ui.btnSalvar.clicked.connect (self.clickedSalvar)
        self.ui.btnCancelar.clicked.connect (self.clickedCancelar)
        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.clicked.connect (self.clicked_table)


    def habilitarJanelas(self, ativo):
        self.ui.btnNovo.setEnabled(ativo)
        self.ui.btnAlterar.setEnabled(ativo)
        self.ui.btnCancelar.setEnabled(not ativo)
        self.ui.btnExcluir.setEnabled(ativo)
        self.ui.btnSalvar.setEnabled(not ativo)
        # txtId.setEnabled(not ativo)
        self.ui.txtEditora.setEnabled(not ativo)

    def limparJanelas(self):
        self.ui.txtId.setText("")
        self.ui.txtEditora.setText("")

    def clickedNovo(self):
        self.habilitarJanelas(False)
        self.limparJanelas()
        self.ui.txtEditora.setFocus()
        self.op = 'N'

    def clickedAlterar(self):
        valores=[]
        self.habilitarJanelas(False)
        self.op = 'A'

        # txtEditora.setText(str(selection[0]))

    def clickedExcluir(self):
        Banco.excluirEditora(self.ui.txtId.text())
        self.carregarTable()

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirEditora(self.ui.txtEditora.text())
        elif self.op == 'A':
            Banco.alterarEditora(self.ui.txtId.text(),
                                 self.ui.txtEditora.text())
        self.habilitarJanelas(True)
        self.carregarTable()

    def clickedCancelar(self):
        self.habilitarJanelas(True)


    def carregarTable(self):
        db = QSqlDatabase().addDatabase('QSQLITE')
        db.setDatabaseName('Litterarius.db')
        if db.open():
            model = QSqlTableModel (self, db)
            model.setTable ("editoras")
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

        db.close()
        QSqlDatabase.removeDatabase('Litterarius.db')

    def carregarDados(self):
        autor = Banco.selectEditoraById(1)

        self.ui.txtId.setText(str(autor))
        self.ui.txtEditora.setText(str(autor))

    def clicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtEditora.setText (str (self.ui.tableView.model().data(index[1])))