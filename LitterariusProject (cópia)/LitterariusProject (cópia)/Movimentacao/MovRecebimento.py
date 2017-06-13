from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QTableView

from UI import Recebimento_ui

class Recebimento(QDialog):
    def __init__(self):
        super(Recebimento, self).__init__()
        self.ui = Recebimento_ui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.tableView.setEditTriggers (QAbstractItemView.NoEditTriggers)
        self.ui.lblDataPago.setText('Pago em: 19/02/2007')

        self.carregarTable()
        self.carregarComboBox()

        self.ui.tableView.setSelectionBehavior (QTableView.SelectRows);
        self.ui.tableView.clicked.connect (self.clicked_table)
        self.ui.cbParcela.currentTextChanged.connect(self.carregarValorParcela)

    def atualizar(self):
        self.carregarTable()
        self.carregarComboBox()

    def carregarValorParcela(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        if db.open ():
            query = QSqlQuery ()
            valores = query.exec ("SELECT vl_parcela, pago FROM recebimentos"
                            " WHERE parcelas_id = %s" % (self.ui.cbParcela.currentText()))
            while query.next():
                print(query.value('vl_parcela'))
            query.first()
            self.ui.txtVlrParcela.setText (str (query.value('vl_parcela')))
            # self.ui.txtVlrParcela.setText (model.data[0])
            # if model.data[1] == 1:
            #     self.ui.cbxPago.setEnabled(True)
            # else:
            #     self.ui.cbxPago.setEnabled(False)
        db.close ()
        QSqlDatabase ().removeDatabase ('Litterarius.db')


    def carregarTable(self):
        db = QSqlDatabase ().addDatabase ('QSQLITE')
        db.setDatabaseName ('Litterarius.db')
        if db.open ():
            query = QSqlQueryModel (self)
            query.setQuery ("SELECT vendas_id as venda, dataVenda as data,"
                            " precoVenda as preco"
                            " FROM vendas")
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
            query.setQuery ("SELECT parcelas_id FROM recebimentos WHERE vendas_id = %s"
                            % (self.ui.txtVendaId.text()))
            model = QSqlTableModel (self, db)
            model.setQuery (query.query ())
            model.select ()
            self.ui.cbParcela.setModel (model)
            self.ui.cbParcela.show ()
        db.close ()
        QSqlDatabase ().removeDatabase ('Litterarius.db')

    def clicked_table(self):
        index = self.ui.tableView.selectedIndexes ()
        modelo = self.ui.tableView.model()
        self.ui.txtVendaId.setText (str (modelo.data (index[0])))
        self.ui.txtPrecoVenda.setText(str(modelo.data(index[2])))
        self.ui.txtDataVenda.setText(modelo.data(index[1]))
        # self.ui.txtTitulo.setText (str (self.ui.tableView.model ().data (index[1])))
        # self.ui.txtISBN.setText (str (self.ui.tableView.model ().data (index[3])))
        # self.ui.txtQTDE.setText (str (self.ui.tableView.model ().data (index[4])))
        # self.ui.txtValor.setText (str (self.ui.tableView.model ().data (index[5])))
        # self.ui.cbEditora.setCurrentText (str (self.ui.tableView.model ().data (index[2])))
        # if self.ui.tableView.model ().data (index[6]) == 1:
        #     self.ui.ckbConsignado.setChecked (True)
        # else:
        #     self.ui.ckbConsignado.setChecked (False)
        self.carregarComboBox()

        return