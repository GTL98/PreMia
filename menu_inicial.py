from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from interface_grafica.interface_grafica_python import menu_inicial
from interface_grafica.interface_grafica_python import res
from tela_ajuda_menu import Ajuda

from acessar_banco_dados import AcessarBancoDados
from criar_banco_dados import CriarBancoDados
from acessar_graficos import AcessarGraficos


class MenuInicial(QWidget, menu_inicial.Ui_menu_inicial):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setWindowTitle('PreMia')

        self.acessar_bd = AcessarBancoDados()
        self.criar_bd = CriarBancoDados()
        self.acessar_graficos_bd = AcessarGraficos()
        self.tela_ajuda = Ajuda()

        # Botão "A c e s s a r"
        self.acessar.clicked.connect(self.acessar_banco_dados)

        # Botão "C r i a r"
        self.criar.clicked.connect(self.criar_banco_dados)

        # Botão "G r á f i c o s"
        self.graficos.clicked.connect(self.acessar_graficos)

        # Botão "A j u d a"
        self.ajuda.clicked.connect(self.botao_ajuda)

        # Botão "V e r s ã o 1.0.0"
        self.versao.clicked.connect(self.botao_versao)

    def acessar_banco_dados(self):
        self.acessar_bd.show()

    def criar_banco_dados(self):
        self.criar_bd.show()

    def acessar_graficos(self):
        self.acessar_graficos_bd.show()

    def botao_ajuda(self):
        self.tela_ajuda.show()

    def botao_versao(self):
        QMessageBox.information(
            self,
            'Dados da versão',
            '''Nome: PreMia
Versão: 1.1.0
Linguagem de programação: Python 3.8.1
Data de lançamento: dd/mm/aaaa
Desenvolvido por: Guilherme Trevisan Linhares
Chave da versão: xxxxxxxxx
O PreMia foi feito com 43 arquivos e 12.277 linhas de código.'''
        )
