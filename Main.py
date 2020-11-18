from PyQt5.QtWidgets import QApplication

from LitterariusHome import LitterariusHome
from MenuLitterarius import MenuLitterarius

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    home = MenuLitterarius()
    sys.exit(app.exec_())

