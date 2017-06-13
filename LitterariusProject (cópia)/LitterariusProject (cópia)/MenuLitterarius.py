import os

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
        file_path = os.path.abspath (os.path.join (os.path.dirname (__file__), "HTMLs/report.html"))
        url = QUrl.fromLocalFile(file_path)
        # self.ui.webView.load (url)
        self.ui.webView.setHtml(htmltopdf.html)
        printer = QPrinter ()
        printer.setPageSize (QPrinter.A4)
        printer.setOutputFormat (QPrinter.PdfFormat)
        printer.setOutputFileName ("file.pdf")
        self.ui.webView.print_ (printer)

        self.ui.btnGerarRel.clicked.connect(self.atualizarRel)

    def atualizarRel(self):
        relatorio = self.ui.cbxRel.currentText()
        tipo = self.ui.cbxTipo.currentText()

        if tipo == 'Livros':
            self.relatorioLivros(tipo)

    def relatorioLivros(self, tipo):
        return

    def render_template(self, template_file, **kwargs):
        template = self.env.get_template(template_file)
        return template.render(**kwargs)

    def print_pdf(self, html, destination):
        self.ui.webView.setHtml(html)
        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(destination)
        self.ui.webView.print_(printer)

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