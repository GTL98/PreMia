import sys
from PyQt5.QtWidgets import QApplication, QWidget
from menu_inicial import MenuInicial


class PreMia:
    def __init__(self):
        self.menu = MenuInicial()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    tela = PreMia()
    # Não precisa o .show() aqui, somente no doc onde está a lógica da tela em questão

    sys.exit(app.exec_())
