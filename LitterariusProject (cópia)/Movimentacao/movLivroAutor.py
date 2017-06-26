from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QDialog

import Banco
from UI import movLivroAutor_ui


class MovLivroAutor(QDialog):
    def __init__(self):
        super(MovLivroAutor, self).__init__()
        self.ui = movLivroAutor_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.carregarListView()

        self.ui.btnIncluir.clicked.connect(self.clickedIncluir)

        # Eventos
        # self.ui.btn

    def limparLista(self):
        self.ui.lwLivroAutor.clear()

    def carregarListView(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        if db.open ():
            self.model = QSqlTableModel (self, db)
            # self.model.setTable ("autores")
            # self.model.select ()
            query = QSqlQueryModel(self)
            query.setQuery("select(autor) from autores")
            self.model.setQuery(query.query())
            self.ui.lvAutor.setModel (self.model)
            self.ui.lvAutor.show ()

        db.close ()

    def clickedIncluir(self):
        for i in self.ui.lvAutor.selectedIndexes():
            self.ui.lwLivroAutor.addItem(str(i.data()))

    def getListWidgetItens(self):
        lista = []
        for i in range (self.ui.lwLivroAutor.count ()):
            lista.append (self.ui.lwLivroAutor.item (i))
        return lista