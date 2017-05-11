from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QMdiSubWindow, QTableView

import Banco
import MtrLivro_ui

# TODO: Função doubleClicked_table()
# TODO: Função carregarDados()

class MtrLivro(QDialog):
    def __init__(self):
        super(MtrLivro, self).__init__()
        self.ui = MtrLivro_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled (False)
        self.ui.txtTitulo.setEnabled (False)
        self.ui.txtQTDE.setEnabled (False)
        self.ui.txtISBN.setEnabled (False)
        self.ui.txtValor.setEnabled (False)
        self.ui.cbAutor.setEnabled (False)
        self.ui.cbEditora.setEnabled (False)
        self.ui.cbGenero.setEnabled (False)

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
        self.ui.txtTitulo.setEnabled(not ativo)
        self.ui.txtQTDE.setEnabled(not ativo)
        self.ui.txtISBN.setEnabled(not ativo)
        self.ui.txtValor.setEnabled(not ativo)
        self.ui.cbGenero.setEnabled(not ativo)
        self.ui.cbAutor.setEnabled(not ativo)
        self.ui.cbEditora.setEnabled(not ativo)

    def limparJanelas(self):
        self.ui.txtId.setText("")
        self.ui.txtTitulo.setText("")
        self.ui.txtQTDE.setText("")
        self.ui.txtValor.setText("")
        self.ui.txtISBN.setText("")
        # self.ui.cbEditora.set("")
        self.ui.cbEditora.set()

    def clickedNovo(self):
        self.habilitarJanelas(False)
        self.limparJanelas()
        self.ui.txtTitulo.setFocus()
        self.op = 'N'

    def clickedAlterar(self):
        valores=[]
        self.habilitarJanelas(False)
        op = 'A'

        # txtEditora.setText(str(selection[0]))

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirLivro(self.ui.txtTitulo.text(), self.ui.txtISBN.text(),
                               self.ui.txtQTDE.text(), self.ui.txtValor.text())
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
            model.setTable ("livros")
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

        db.close()

    def carregarDados(self):
        livro = Banco.selectLivroById(1)

        self.ui.txtId.setText(str(livro[0]))
        self.ui.txtTitulo.setText(str(livro[1]))

    def doubleClicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        # livros = Banco.selectLivrosById(index)
        # print(str(index))
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtTitulo.setText (str (self.ui.tableView.model().data(index[1])))