from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QDialog, QTableView, QAbstractItemView

import Banco
from UI import MtrLivro_ui
from Movimentacao.movLivroAutor import MovLivroAutor
from Movimentacao.movLivroGen import MovLivroGen


# TODO: carregar listWidget do livro selecionado
# TODO: verificar se ja tem livro no banco com esse nome

class MtrLivro(QDialog):
    def __init__(self):
        super(MtrLivro, self).__init__()
        self.ui = MtrLivro_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled(False)
        self.habilitarJanelas(False)

        self.ui.tableView.setEditTriggers (QAbstractItemView.NoEditTriggers)
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
        self.ui.tbGenero.clicked.connect(self.clickedLivroGen)
        self.ui.tbAutor.clicked.connect(self.clickedLivroAutor)

        self.movLivroGen = MovLivroGen()
        self.movLivroAutor = MovLivroAutor()

    def clickedLivroGen(self):
        self.movLivroGen.exec_()

    def clickedLivroAutor(self):
        self.movLivroAutor.exec_()

    def habilitarJanelas(self, ativo):
        self.ui.btnNovo.setEnabled(ativo)
        self.ui.btnAlterar.setEnabled(ativo)
        self.ui.btnCancelar.setEnabled(not ativo)
        self.ui.btnExcluir.setEnabled(ativo)
        self.ui.btnSalvar.setEnabled(not ativo)
        # txtId.setEnabled(not ativo)
        self.ui.txtTitulo.setEnabled(not ativo)
        self.ui.txtQTDE.setEnabled(not ativo)
        self.ui.txtISBN.setEnabled(not ativo)
        self.ui.txtValor.setEnabled(not ativo)
        self.ui.tbGenero.setEnabled(not ativo)
        self.ui.tbAutor.setEnabled(not ativo)
        self.ui.cbEditora.setEnabled(not ativo)
        self.ui.ckbConsignado.setEnabled(not ativo)

    def limparJanelas(self):
        self.ui.txtId.setText("")
        self.ui.txtTitulo.setText("")
        self.ui.txtQTDE.setText("")
        self.ui.txtValor.setText("")
        self.ui.txtISBN.setText("")
        # self.ui.cbEditora.set("")
        self.ui.cbEditora.setCurrentText("")

    def clickedNovo(self):
        self.habilitarJanelas(False)
        self.limparJanelas()
        self.ui.txtTitulo.setFocus()
        self.op = 'N'

    def clickedAlterar(self):
        valores=[]
        self.habilitarJanelas(False)
        self.op = 'A'

        # txtEditora.setText(str(selection[0]))

    def clickedExcluir(self):
        Banco.excluirLivro(self.ui.txtId.text())
        self.carregarTable()

    def clickedSalvar(self):
        contador = 0
        if self.op == 'N':
            contador = 0
            Banco.inserirLivro(self.ui.txtTitulo.text(), self.ui.cbEditora.currentText(),
                               self.ui.txtISBN.text(), self.ui.txtQTDE.text(),
                               self.ui.txtValor.text(), self.ui.ckbConsignado.isChecked())

            # verificar se tem generos a inserir
            for genero in self.movLivroGen.getListWidgetItens():
                contador+=1
            if contador > 0:
                for genero in self.movLivroGen.getListWidgetItens():
                    Banco.inserirLivrosGeneros(self.ui.txtId.text(), genero.text())

            #  verificar se tem autores a inserir
            for autor in self.movLivroAutor.getListWidgetItens():
                contador+=1
            if contador > 0:
                for autor in self.movLivroAutor.getListWidgetItens():
                    Banco.inserirLivrosAutores(self.ui.txtId.text(), autor.text())

        elif self.op == 'A':
            Banco.alterarLivro(self.ui.txtId.text(), self.ui.txtTitulo.text(),
                               self.ui.cbEditora.currentText(),
                               self.ui.txtISBN.text(), self.ui.txtQTDE.text(),
                               self.ui.txtValor.text(), self.ui.ckbConsignado.isChecked())

        self.habilitarJanelas(True)
        self.carregarTable()

    def clickedCancelar(self):
        self.habilitarJanelas(True)


    def carregarTable(self):
        db = QSqlDatabase().addDatabase('QSQLITE')
        db.setDatabaseName('Litterarius.db')
        conexao = db.connectionName()
        if db.open():
            query = QSqlQueryModel(self)
            query.setQuery("SELECT"
                           " livros_id, titulo, editoras.editora,"
                           " isbn, qtde_estoque, vl_unitario, consignado"
                           " FROM livros"
                           " INNER JOIN editoras ON livros.editoras_fk = editoras.editoras_id")
            model = QSqlTableModel (self, db)
            model.setQuery (query.query())
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

            # carregar combobox de editoras
            query2 = QSqlQueryModel(self)
            query2.setQuery("select(editora) from editoras")
            model2 = QSqlTableModel (self, db)
            model2.setQuery(query2.query())
            model2.select()
            self.ui.cbEditora.setModel(model2)
        db.close()

    def carregarDados(self):
        livro = Banco.selectLivroById(1)

        self.ui.txtId.setText(str(livro[0]))
        self.ui.txtTitulo.setText(str(livro[1]))

    def clicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtTitulo.setText (str (self.ui.tableView.model().data(index[1])))
        self.ui.txtISBN.setText (str (self.ui.tableView.model().data(index[3])))
        self.ui.txtQTDE.setText (str (self.ui.tableView.model().data(index[4])))
        self.ui.txtValor.setText (str (self.ui.tableView.model().data(index[5])))
        self.ui.cbEditora.setCurrentText (str (self.ui.tableView.model().data(index[2])))
        if self.ui.tableView.model ().data (index[6]) == 1:
            self.ui.ckbConsignado.setChecked (True)
        else:
            self.ui.ckbConsignado.setChecked (False)