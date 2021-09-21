from PyQt5.QtWidgets import QWidget
from interface_grafica.interface_grafica_python import tela_ajuda


class Ajuda(QWidget, tela_ajuda.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
