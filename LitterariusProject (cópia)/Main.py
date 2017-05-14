from PyQt5.QtWidgets import QApplication

from LitterariusHome import LitterariusHome

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    home = LitterariusHome()
    sys.exit(app.exec_())

