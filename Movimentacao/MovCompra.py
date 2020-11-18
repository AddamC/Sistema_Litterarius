from PyQt5 import QtGui

from PyQt5.QtCore import QObject, Qt, QPoint

from PyQt5.QtSql import QSqlTableModel, QSqlQueryModel, QSqlDatabase
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QHeaderView, QTableWidgetItem

import Banco
from Movimentacao.ConfPagamento import ConfPagamento
from UI import Compra_ui
from Movimentacao.MovBuscarLivro import MovBuscarLivro

class Compra(QDialog):
    def __init__(self):
        super(Compra, self).__init__()
        self.ui = Compra_ui.Ui_Form()
        self.ui.setupUi (self)

        self.ui.tvLivros.setEditTriggers (QAbstractItemView.NoEditTriggers)

        # definir valores
        self.carregarValores()
        self.precoCompra = 0
        self.ui.lblPreco.setText(str(self.precoCompra))
        self.ui.lblInformacao.hide()

        self.ui.tvLivros.alternatingRowColors ()
        self.ui.tvLivros.selectRow(1)
        self.ui.txtPesquisar.textChanged.connect (self.carregarDados)

        self.ui.tvLivros.setSelectionBehavior (QAbstractItemView.SelectRows);
        # self.ui.tvLivros.clicked.connect(self.carregarSlider)

        self.ui.tvLivros.doubleClicked.connect (self.addNoCarrinho)
        self.ui.btnAddLivro.clicked.connect(self.addNoCarrinho)
        self.ui.btnContinuar.clicked.connect(self.clickedContinuar)

        self.ui.sldQtde.valueChanged.connect(self.aumentarQtde)

        self.ui.rbEditora.setChecked (True)

        self.buscarLivro = MovBuscarLivro()
        self.conf_pagamento = ConfPagamento()

    def atualizar(self):
        self.carregarValores()
        self.precoCompra = 0
        self.ui.lblPreco.setText(str(self.precoCompra))
        self.ui.lblInformacao.hide()

    def esvaziarCarrinho(self):
        return

    def carregarSlider(self):
        index = self.ui.tvLivros.selectedIndexes()
        modelo = self.ui.tvLivros.model()
        self.ui.sldQtde.setMaximum(modelo.data(index[2]))

    def carregarValores(self):
        self.carregarTable ()
        self.carregarComboBox()
        self.modelarTableCarrinho()
        self.ui.sbQTDE.setValue(self.ui.sldQtde.value())

    def modelarTableCarrinho(self):
        model = QSqlTableModel()

        self.ui.sldQtde.setMinimum(1)
        self.ui.sldQtde.setMaximum (100)

        self.ui.twCarrinho.setColumnCount(3)
        self.ui.twCarrinho.setHorizontalHeaderLabels(["livro", "QTDE", "Preço"])
        self.ui.twCarrinho.show()

    def aumentarQtde(self):
        index = self.ui.tvLivros.selectedIndexes()
        modelo = self.ui.tvLivros.model()
        self.ui.sbQTDE.setValue(self.ui.sldQtde.value())
        # self.ui.lblPreco.setText(str(int(self.ui.sbQTDE.text()) * int(modelo.data(index[3]))))

    def clickedContinuar(self):
        self.conf_pagamento.atualizar(float(self.ui.lblPreco.text()))
        self.conf_pagamento.exec_()
        if self.conf_pagamento.confirmado:
            Banco.inserirCompra(self.ui.cbxFornecedores.currentText(), self.ui.lblPreco.text())
            qtde = None
            valor =None
            livro = None
            carrinho = self.ui.twCarrinho

            for i in range(self.ui.twCarrinho.rowCount()):
                livro = carrinho.item(i, 0).text()
                qtde = carrinho.item(i, 1).text()
                preco = carrinho.item(i, 2).text()
                Banco.inserirDetCompra(qtde, preco, livro)

            self.carregarTable()
            self.esvaziarCarrinho()

    def addNoCarrinho(self):
        index = self.ui.tvLivros.selectedIndexes()
        modelo = self.ui.tvLivros.model ()

        livro = QTableWidgetItem(modelo.data (index[0]))
        qtde = QTableWidgetItem (self.ui.sbQTDE.text())
        preco = float(self.ui.sbQTDE.text()) * modelo.data(index[3])
        self.precoCompra = self.precoCompra + preco
        self.ui.lblPreco.setText(str(self.precoCompra))

        preco = QTableWidgetItem(str(preco)) # convertendo pra item de tabela

        self.ui.twCarrinho.insertRow(self.ui.twCarrinho.rowCount())
        self.ui.twCarrinho.setItem(self.ui.twCarrinho.rowCount()-1, 0, livro)
        self.ui.twCarrinho.setItem(self.ui.twCarrinho.rowCount()-1, 1, qtde)
        self.ui.twCarrinho.setItem(self.ui.twCarrinho.rowCount()-1, 2, preco)


    def carregarDados(self):
        if self.ui.txtPesquisar.text() == "":
            self.carregarTable()

        elif self.ui.rbAutor.isChecked():
            self.carregarTableByAutor()

        elif self.ui.rbEditora.isChecked():
            self.carregarTableByEditora()

        elif self.ui.rbTitulo.isChecked():
            self.carregarTableByTitulo()

    def carregarComboBox(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        conexao = db.connectionName ()
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT"
                            " fornecedor"
                            " FROM fornecedores")
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.cbxFornecedores.setModel (model)
            self.ui.cbxFornecedores.show ()
        db.close ()

    def carregarTable(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        conexao = db.connectionName ()
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT"
                            " titulo, editoras.editora,"
                            " qtde_estoque, vl_unitario, consignado"
                            " FROM livros"
                            " INNER JOIN editoras ON livros.editoras_fk = editoras.editoras_id")
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.tvLivros.setModel (model)
            self.ui.tvLivros.show ()
        db.close()

    def carregarTableByAutor(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        conexao = db.connectionName ()
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT"
                            " titulo, editoras.editora,"
                            " qtde_estoque, vl_unitario, consignado"
                            " FROM livros"
                            " INNER JOIN editoras ON livros.editoras_fk = editoras.editoras_id"
                            " WHERE livros_id =("
                            " SELECT livros_id FROM livros_autores WHERE autores_id=("
                            "       SELECT autores_id FROM autores WHERE autor LIKE '%s'))"

                            % (self.ui.txtPesquisar.text()+"%"))
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.tvLivros.setModel (model)
            self.ui.tvLivros.show ()

        db.close ()

    def carregarTableByTitulo(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        conexao = db.connectionName ()
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT"
                            " titulo, editoras.editora,"
                            " qtde_estoque, vl_unitario, consignado"
                            " FROM livros"
                            " INNER JOIN editoras ON livros.editoras_fk = editoras.editoras_id"
                            " WHERE titulo LIKE '%s'"
                            % (self.ui.txtPesquisar.text()+"%"))
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.tvLivros.setModel (model)
            self.ui.tvLivros.show ()

        db.close ()



    def carregarTableByGenero(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        conexao = db.connectionName ()
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT"
                            " titulo, editoras.editora,"
                            " qtde_estoque, vl_unitario, consignado"
                            " FROM livros"
                            " INNER JOIN editoras ON livros.editoras_fk = editoras.editoras_id"
                            " WHERE livros_id =("
                            " SELECT livros_id FROM livros_generos WHERE generos_id=("
                            "       SELECT generos_id FROM generos WHERE genero LIKE '%s'))"

                            % (self.ui.txtPesquisar.text()+"%"))
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.tvLivros.setModel (model)
            self.ui.tvLivros.show ()

        db.close ()


    def carregarTableByEditora(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        conexao = db.connectionName ()
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT"
                            " titulo, editoras.editora,"
                            " qtde_estoque, vl_unitario, consignado"
                            " FROM livros"
                            " INNER JOIN editoras ON livros.editoras_fk = editoras.editoras_id"
                            " WHERE editoras.editora LIKE '%s'"
                            % (self.ui.txtPesquisar.text ()+"%"))
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.tvLivros.setModel (model)
            self.ui.tvLivros.show ()
        db.close ()

    def getTableWidgetItens(self):
        lista = []
        for i in range (self.ui.twCarrinho.rowCount()):
            lista.append (self.ui.lwCarrinho.item (i))
        return lista
