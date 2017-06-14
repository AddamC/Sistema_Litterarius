from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QDialog, QTableView

from UI import Pagamento_ui

class Pagamento(QDialog):
    def __init__(self):
        super(Pagamento, self).__init__()
        self.ui = Pagamento_ui.Ui_Form()
        self.ui.setupUi(self)

        self.carregarTable()
        self.carregarComboBox ()

        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.clicked.connect (self.clicked_table)

    def atualizar(self):
        self.carregarTable()

    def carregarTable(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT compras_id as compra, dataCompra as data,"
                            " precoCompra as preco"
                            " FROM compras")
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.tableView.setModel (model)
            self.ui.tableView.show ()
        db.close ()
        QSqlDatabase ().removeDatabase ('Litterarius.db')

    def carregarComboBox(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT parcelas_id FROM pagamentos WHERE compras_id = %s"
                            % (self.ui.txtCompraId.text ()))
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.cbParcela.setModel (model)
            self.ui.cbParcela.show ()
        db.close ()
        QSqlDatabase ().removeDatabase ('Litterarius.db')

    def clicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        self.ui.txtCompraId.setText (str (self.ui.tableView.model ().data (index[0])))
        # self.ui.txtTitulo.setText (str (self.ui.tableView.model ().data (index[1])))
        # self.ui.txtISBN.setText (str (self.ui.tableView.model ().data (index[3])))
        # self.ui.txtQTDE.setText (str (self.ui.tableView.model ().data (index[4])))
        # self.ui.txtValor.setText (str (self.ui.tableView.model ().data (index[5])))
        # self.ui.cbEditora.setCurrentText (str (self.ui.tableView.model ().data (index[2])))
        # if self.ui.tableView.model ().data (index[6]) == 1:
        #     self.ui.ckbConsignado.setChecked (True)
        # else:
        #     self.ui.ckbConsignado.setChecked (False)
        self.carregarComboBox ()

        return