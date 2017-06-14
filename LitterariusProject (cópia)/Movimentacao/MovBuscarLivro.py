from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QAbstractItemView

import Banco
from UI import BuscarLivro_ui

class MovBuscarLivro(QDialog):
    def __init__(self):
        super(MovBuscarLivro, self).__init__()
        self.ui = BuscarLivro_ui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.tableView.setEditTriggers (QAbstractItemView.NoEditTriggers)
        self.carregarTable()
        self.ui.tableView.alternatingRowColors()
        self.ui.txtPesquisar.textChanged.connect(self.carregarDados)

        self.listaLivros = []

        self.ui.tableView.doubleClicked.connect(self.preencherLista)

        self.ui.rbEditora.setChecked(True)

        # self.ui.tableView.doubleClicked()

    def preencherLista(self):

        for i in self.ui.tableView.selectedIndexes():
            print(i.data())
        # self.listaLivros.append(self.ui.tableView.selectedIndexes())
        # for i in self.listaLivros:
        #     print(i.data())

    def carregarDados(self):
        if self.ui.txtPesquisar.text() == "":
            self.carregarTable()

        elif self.ui.rbAutor.isChecked():
            self.carregarTableByAutor()

        elif self.ui.rbEditora.isChecked():
            self.carregarTableByEditora()

        elif self.ui.rbTitulo.isChecked():
            self.carregarTableByTitulo()


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
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()
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
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

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
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

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
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()

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
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()
        db.close ()
