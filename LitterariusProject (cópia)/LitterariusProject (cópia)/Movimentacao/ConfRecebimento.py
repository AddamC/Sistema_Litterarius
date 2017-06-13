from PyQt5.QtWidgets import QDialog

import Banco
from UI import ConfPagamento_ui

class ConfRecebimento(QDialog):
    preco_total = None
    confirmado = None

    def __init__(self):
        super(ConfRecebimento, self).__init__()
        self.ui = ConfPagamento_ui.Ui_Form()
        self.ui.setupUi(self)

        # self.preco_total = preco_total
        self.confirmado = False

        self.ui.cbxParcelas.setEnabled(False)

        self.ui.rbCartao.setChecked(True)
        self.ui.rbVista.setChecked(True)
        self.ui.rbParcelado.clicked.connect(self.ativarParcela)
        self.ui.rbVista.clicked.connect(self.desativarParcela)
        self.ui.btnConfirmar.clicked.connect(self.clickedConfirmar)

        self.carregarComboBox()

    def atualizar(self, preco_total):
        self.preco_total = preco_total

    def clickedConfirmar(self):
        valor_parcela = float(self.preco_total/
                             int(self.ui.cbxParcelas.currentText()))
        print(str(valor_parcela))


        for i in range(int(self.ui.cbxParcelas.currentText())):
            if self.ui.rbParcelado.isChecked():
                Banco.gerarRecebimento(i, valor_parcela)
                print(i)
        self.confirmado = True
        self.close()

    def carregarComboBox(self):
        for i in range(1, 12):
            self.ui.cbxParcelas.addItem(str(i))

    def ativarParcela(self):
        self.ui.cbxParcelas.setEnabled(True)

    def desativarParcela(self):
        self.ui.cbxParcelas.setEnabled(False)
