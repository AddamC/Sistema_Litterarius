from PyQt5.QtWidgets import QDialog, QMdiSubWindow

from UI import Litterarius_ui
from UI.Manter_ui import Manter
from Movimentacao.MenuMovimentacao import MenuMovimentacao


class LitterariusHome(QDialog):
    def __init__(self):
        super(LitterariusHome, self).__init__()
        ui = Litterarius_ui.Ui_Dialog ()
        ui.setupUi(self)
        ui.btnManter.clicked.connect(self.clickedManter)

        janelaManter = QMdiSubWindow ()
        manter = Manter ()
        movimentacao = MenuMovimentacao()
        janelaManter.setWidget (movimentacao)
        janelaManter.setGeometry (0, 0, 780, 500)

        ui.mdiArea.addSubWindow (janelaManter)

        # janelaManter.show ()

        self.show()

    def clickedManter(self):
        print("ola")
