import traceback

from PyQt5 import Qt

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QDialog, QTableView, QAbstractItemView

import Banco
from UI import MtrFornecedor_ui


class MtrFornecedor(QDialog):
    def __init__(self):
        super(MtrFornecedor, self).__init__()
        self.ui = MtrFornecedor_ui.Ui_Form ()
        self.ui.setupUi(self)

        self.op = ''
        self.ui.txtId.setEnabled (False)
        self.ui.txtCNPJ.setEnabled (False)
        self.ui.txtFornecedor.setEnabled (False)


        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.carregarTable ()
        self.carregarDados ()
        self.habilitarJanelas (True)

        # Eventos
        self.ui.btnNovo.clicked.connect (self.clickedNovo)
        self.ui.btnAlterar.clicked.connect (self.clickedAlterar)
        self.ui.btnSalvar.clicked.connect (self.clickedSalvar)
        self.ui.btnCancelar.clicked.connect (self.clickedCancelar)
        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.clicked.connect (self.clicked_table)
        # try:
        #     db = QSqlDatabase.addDatabase ("QSQLITE");
        #     db.setDatabaseName ("Litterarius.db");
        #     if db.open:
        #         model = QSqlQueryModel ();
        #         model.setQuery ("SELECT fornecedor FROM fornecedores")
        #         # model.setHeaderData (0, Qt.Horizontal, tr ("id"));
        #         # model.setHeaderData (1, Qt.Horizontal, tr ("test"));
        #
        #         self.ui.cbTransportadora.setModel (model);
        #         db.close()
        #         QSqlDatabase.removeDatabase("Litterarius.db")
        # # self.ui.cbTransportadora.setView (self.ui.tableView);
        # except:
        #     traceback.prin_exec()

    def habilitarJanelas(self, ativo):
        self.ui.btnNovo.setEnabled(ativo)
        self.ui.btnAlterar.setEnabled(ativo)
        self.ui.btnCancelar.setEnabled(not ativo)
        self.ui.btnExcluir.setEnabled(ativo)
        self.ui.btnSalvar.setEnabled(not ativo)
        # txtId.setEnabled(not ativo)
        self.ui.txtFornecedor.setEnabled(not ativo)
        self.ui.txtCNPJ.setEnabled (not ativo)
        self.ui.cbTransportadora.setEnabled(not ativo)

    def limparJanelas(self):
        self.ui.txtId.setText("")
        self.ui.txtFornecedor.setText("")
        self.ui.txtCNPJ.setText("")

    def clickedNovo(self):
        self.habilitarJanelas(False)
        self.limparJanelas()
        self.ui.txtFornecedor.setFocus()
        self.ui.txtCNPJ.setFocus()
        self.op = 'N'

    def clickedAlterar(self):
        valores=[]
        self.habilitarJanelas(False)
        op = 'A'

        # txtAutor.setText(str(selection[0]))

    def clickedSalvar(self):
        if self.op == 'N':
            Banco.inserirFornecedor(self.ui.txtFornecedor.text(),
                                    self.ui.txtCNPJ.text(),
                                    self.ui.cbTransportadora.text())
        elif self.op == 'A':
            Banco.alterarFornecedor(self.ui.txtId.text(),
                                    self.ui.txtFornecedor.text(),
                                    self.ui.txtCNPJ.text(),
                                    self.ui.cbTransportadora.text())
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
            model2 = QSqlTableModel (self, db)
            model.setTable ("fornecedores")
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()
            model2.setTable("transportadoras")
            model2.select()
            self.ui.cbTransportadora.setModel(model2)
            self.ui.cbTransportadora.setModelColumn (1)
        db.close()
        QSqlDatabase().removeDatabase('Litterarius.db')


    def carregarDados(self):
        autor = Banco.selectAutorById(1)

        self.ui.txtId.setText(str(autor))
        self.ui.txtFornecedor.setText(str(autor))
        # self.ui.txtCNPJ.setText (str (autor[2]))

    def clicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtId.setText (str (self.ui.tableView.model().data(index[0])))
        self.ui.txtFornecedor.setText (str (self.ui.tableView.model().data(index[1])))
        self.ui.txtCNPJ.setText (str (self.ui.tableView.model().data(index[2])))