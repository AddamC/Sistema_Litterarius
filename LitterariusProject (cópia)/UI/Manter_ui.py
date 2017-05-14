from PyQt5 import Qt

import PyQt5
from Manter.MtrAutor import MtrAutor
from Manter.MtrCliente import MtrCliente
from Manter.MtrEditora import MtrEditora
from Manter.MtrFornecedor import MtrFornecedor
from Manter.MtrFuncionario import MtrFuncionario
from Manter.MtrLivro import MtrLivro
from Manter.MtrTransportadora import MtrTransportadora
from PyQt5.QtWidgets import *

from Manter.MtrGenero import MtrGenero


class Manter (QWidget):

    def __init__(self):
        super (Manter, self).__init__ ()
        self.showFullScreen()
        self.layoutManter = PyQt5.QtWidgets.QVBoxLayout ()

        self.btnLivro = PyQt5.QtWidgets.QPushButton ('livros')
        self.btnLivro.sizeHint ()
        self.btnEditora = PyQt5.QtWidgets.QPushButton ('Editora')
        self.btnEditora.sizeHint ()
        self.btnAutor = PyQt5.QtWidgets.QPushButton ('Autor')
        self.btnAutor.sizeHint ()
        self.btnGenero = PyQt5.QtWidgets.QPushButton ('Gênero')
        self.btnGenero.sizeHint ()
        self.btnCliente = PyQt5.QtWidgets.QPushButton ('Cliente')
        self.btnCliente.sizeHint ()
        self.btnFuncionario = QPushButton ('Funcionario')
        self.btnFuncionario.sizeHint ()
        self.btnFornecedor = QPushButton ('Fornecedor')
        self.btnFornecedor.sizeHint ()
        self.btnTransportadora = QPushButton ('Transportadora')

        self.btnGenero.sizeHint ()
        self.layoutManter.addWidget (self.btnLivro)
        self.layoutManter.addWidget (self.btnEditora)
        self.layoutManter.addWidget (self.btnAutor)
        self.layoutManter.addWidget (self.btnGenero)
        self.layoutManter.addWidget (self.btnFuncionario)
        self.layoutManter.addWidget (self.btnCliente)
        self.layoutManter.addWidget (self.btnFornecedor)

        self.setLayout(self.layoutManter)

        self.btnLivro.clicked.connect (self.clickLivro)
        self.btnAutor.clicked.connect (self.clickAutor)
        self.btnEditora.clicked.connect (self.clickEditora)
        self.btnCliente.clicked.connect (self.clickCliente)
        self.btnFuncionario.clicked.connect(self.clickFuncionario)
        self.btnFornecedor.clicked.connect(self.clickFornecedor)
        self.btnTransportadora.clicked.connect(self.clickTransportadora)
        self.btnGenero.clicked.connect(self.clickGenero)

        self.mtrLivro = MtrLivro()
        self.mtrEditora = MtrEditora()
        self.mtrAutor = MtrAutor()
        self.mtrGenero = MtrGenero()
        self.mtrCliente = MtrCliente()
        self.mtrFunc = MtrFuncionario()
        self.mtrForn = MtrFornecedor()
        self.mtrTransp = MtrTransportadora()

    def clickLivro(self):
        self.mtrLivro.exec_()

    def clickAutor(self):
        self.mtrAutor.exec_()

    def clickEditora(self):
        self.mtrEditora.exec_()

    def clickCliente(self):
        self.mtrCliente.exec_()

    def clickFuncionario(self):
        self.mtrFunc.exec_()

    def clickFornecedor(self):
        self.mtrForn.exec_()

    def clickTransportadora(self):
        self.mtrTransp.exec_()

    def clickGenero(self):
        self.mtrGenero.exec_()


    def switch(self, l):
        return self.dict[l]