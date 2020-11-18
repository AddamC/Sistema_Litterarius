import sqlite3
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QDialog, QTableView

import Banco
from UI import movLivroGen_ui


class MovLivroGen(QDialog):
    def __init__(self):
        super(MovLivroGen, self).__init__()
        self.ui = movLivroGen_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.listGenero = []
        # self.livro = livroId

        self.carregarListView()

    def limparLista(self):
        self.ui.lwLivroGenero.clear()


    def addFromDB(self, idLivro):
        self.limparLista()
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        generos = cursor.execute("SELECT generos.genero FROM livros_generos "
                       " inner join generos "
                       " on generos.generos_id = livros_generos.generos_id "
                       " where livros_generos.livros_id = 1;")
        for i in generos.fetchall():
            print(i)
            self.ui.lwLivroGenero.addItem(i)

    def carregarListView(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        if db.open ():
            self.model = QSqlTableModel (self, db)
            # self.model.setTable ("autores")
            # self.model.select ()
            query = QSqlQueryModel(self)
            query.setQuery("select(genero) from generos")
            self.model.setQuery(query.query())
            self.ui.lvGenero.setModel (self.model)
            self.ui.lvGenero.show ()

            self.ui.btnIncluir.clicked.connect(self.clickedIncluir)

        db.close ()

    def clickedIncluir(self):
        for i in self.ui.lvGenero.selectedIndexes():
            self.ui.lwLivroGenero.addItem(str(i.data()))

    def getListWidgetItens(self):
        lista = []
        for i in range(self.ui.lwLivroGenero.count()):
            lista.append(self.ui.lwLivroGenero.item(i))
        return lista