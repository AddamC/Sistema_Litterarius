import PyQt5
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton

from UI import Movimentacao_ui
from Movimentacao.MovVenda import Venda
from Movimentacao.MovCompra import Compra
from Movimentacao.MovRecebimento import Recebimento
from Movimentacao.MovPagamento import Pagamento


class MenuMovimentacao(QWidget):
    def __init__(self):
        super (MenuMovimentacao, self).__init__ ()
        self.ui = Movimentacao_ui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.btnDetCompra.clicked.connect (self.clickCompra)
        self.ui.btnDetVenda.clicked.connect (self.clickVenda)
        self.ui.btnRecebimento.clicked.connect (self.clickRecebimento)
        self.ui.btnPagamento.clicked.connect (self.clickPagamento)

        self.detCompra = Compra()
        self.detVenda = Venda()
        self.pagamento = Pagamento()
        self.recebimento = Recebimento()

    def clickCompra(self):
        self.detCompra.atualizar()
        self.detCompra.exec_()

    def clickVenda(self):
        self.detVenda.atualizar()
        self.detVenda.exec_()

    def clickPagamento(self):
        self.pagamento.exec_()

    def clickRecebimento(self):
        self.recebimento.exec_()

        # self.showFullScreen()
        # self.layoutManter = PyQt5.QtWidgets.QVBoxLayout ()
        #
        # self.btnDetCompra = PyQt5.QtWidgets.QPushButton ('DetCompra')
        # self.btnDetCompra.sizeHint ()
        # self.btnDetVenda = PyQt5.QtWidgets.QPushButton ('DetVenda')
        # self.btnDetVenda.sizeHint ()
        # self.btnRecebimento = PyQt5.QtWidgets.QPushButton ('Recebimento')
        # self.btnRecebimento.sizeHint ()
        # self.btnPagamento = PyQt5.QtWidgets.QPushButton ('Pagamento')
        # self.btnPagamento.sizeHint ()
        #
        # self.layoutManter.addWidget (self.btnDetCompra)
        # self.layoutManter.addWidget (self.btnDetVenda)
        # self.layoutManter.addWidget (self.btnRecebimento)
        # self.layoutManter.addWidget (self.btnPagamento)
        #
        # self.setLayout(self.layoutManter)
        #
        # self.btnDetCompra.clicked.connect (self.clickLivro)
        # self.btnDetVenda.clicked.connect (self.clickAutor)
        # self.btnRecebimento.clicked.connect (self.clickEditora)
        # self.btnPagamento.clicked.connect (self.clickCliente)
        #
        # self.detVenda = MovVenda()
        # self.detCompra = MovCompra()