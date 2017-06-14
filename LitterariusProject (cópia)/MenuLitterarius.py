import os

import sqlite3

import pandas as pd
from PyQt5.QtCore import QUrl
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QDialog, QMdiSubWindow

import htmltopdf
from Movimentacao.MovCompra import Compra
from Movimentacao.MovPagamento import Pagamento
from Movimentacao.MovRecebimento import Recebimento
from Movimentacao.MovVenda import Venda
from UI import MenuLitterarius_ui
from UI.Manter_ui import Manter
from Movimentacao.MenuMovimentacao import MenuMovimentacao

from Manter.MtrGenero import MtrGenero
from Manter.MtrAutor import MtrAutor
from Manter.MtrCliente import MtrCliente
from Manter.MtrEditora import MtrEditora
from Manter.MtrFornecedor import MtrFornecedor
from Manter.MtrFuncionario import MtrFuncionario
from Manter.MtrLivro import MtrLivro
from Manter.MtrTransportadora import MtrTransportadora

from jinja2 import Environment, PackageLoader

class MenuLitterarius(QDialog):
    def __init__(self):
        super(MenuLitterarius, self).__init__()
        self.ui = MenuLitterarius_ui.Ui_Dialog ()
        self.ui.setupUi(self)
        self.show()

        self.carregarComboBox()

        # Manter
        self.ui.btnLivros.clicked.connect (self.clickLivro)
        self.ui.btnAutores.clicked.connect (self.clickAutor)
        self.ui.btnEditoras.clicked.connect (self.clickEditora)
        self.ui.btnClientes.clicked.connect (self.clickCliente)
        self.ui.btnFuncionarios.clicked.connect (self.clickFuncionario)
        self.ui.btnFornecedores.clicked.connect (self.clickFornecedor)
        self.ui.btnTransportadoras.clicked.connect (self.clickTransportadora)
        self.ui.btnGeneros.clicked.connect (self.clickGenero)

        self.mtrLivro = MtrLivro ()
        self.mtrEditora = MtrEditora ()
        self.mtrAutor = MtrAutor ()
        self.mtrGenero = MtrGenero ()
        self.mtrCliente = MtrCliente ()
        self.mtrFunc = MtrFuncionario ()
        self.mtrForn = MtrFornecedor ()
        self.mtrTransp = MtrTransportadora ()

        # Movimentar
        self.ui.btnDetCompra.clicked.connect (self.clickCompra)
        self.ui.btnDetVenda.clicked.connect (self.clickVenda)
        self.ui.btnRecebimento.clicked.connect (self.clickRecebimento)
        self.ui.btnPagamento.clicked.connect (self.clickPagamento)

        self.detCompra = Compra ()
        self.detVenda = Venda ()
        self.pagamento = Pagamento ()
        self.recebimento = Recebimento ()

        # Relatorio
        self.html = None
        self.atualizarRel()
        printer = QPrinter ()
        printer.setPageSize (QPrinter.A4)
        printer.setOutputFormat (QPrinter.PdfFormat)
        printer.setOutputFileName ("file.pdf")
        self.ui.webView.print_ (printer)

        self.ui.btnGerarRel.clicked.connect(self.atualizarRel)

    def color_negative_red(self):
        color = 'red'
        return "color: %s" % color

    def atualizarRel(self):
        conn = sqlite3.connect ("Litterarius.db")
        relatorio = self.ui.cbxRel.currentText()
        tipo = self.ui.cbxTipo.currentText()

        if not relatorio == 'Livros':
            df = pd.read_sql_query (" SELECT livros.titulo, generos.genero FROM livros_generos "
                                    " INNER JOIN livros "
                                    " on livros_generos.livros_id = livros.livros_id"
                                    " INNER JOIN generos "
                                    " on livros_generos.generos_id = generos.generos_id", conn)

        try:
            if not self.ui.txtSql.text () == '':
                df = pd.read_sql_query (self.ui.txtSql.text (), conn)
            elif self.ui.txtRel.text () == '':
                return
            else:
                df = pd.read_sql_query (" SELECT * FROM %s " % (self.ui.txtRel.text ()), conn)
        except:
            return

        s = df.style.highlight_null().render().split('\n')[:10]
        self.html = df.to_html
        self.ui.webView.setHtml (self.html)

    def clickLivro(self):
        self.mtrLivro.exec_ ()

    def clickAutor(self):
        self.mtrAutor.exec_ ()

    def clickEditora(self):
        self.mtrEditora.exec_ ()

    def clickCliente(self):
        self.mtrCliente.exec_ ()

    def clickFuncionario(self):
        self.mtrFunc.exec_ ()

    def clickFornecedor(self):
        self.mtrForn.exec_ ()

    def clickTransportadora(self):
        self.mtrTransp.exec_ ()

    def clickGenero(self):
        self.mtrGenero.exec_ ()

    def clickCompra(self):
        self.detCompra.exec_()

    def clickVenda(self):
        self.detVenda.exec_()

    def clickPagamento(self):
        self.pagamento.atualizar()
        self.pagamento.exec_()

    def clickRecebimento(self):
        self.recebimento.atualizar()
        self.recebimento.exec_()

    def carregarComboBox(self):
        self.ui.cbxRel.addItem('Livros')
        self.ui.cbxTipo.addItem('Por Categoria')