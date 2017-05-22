from PyQt5.QtWidgets import QDialog

from UI import Pagamento_ui

class Pagamento(QDialog):
    def __init__(self):
        super(Pagamento, self).__init__()
        self.ui = Pagamento_ui.Ui_Form ()
        self.ui.setupUi (self)

