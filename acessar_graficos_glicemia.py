from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from interface_grafica.interface_grafica_python import tela_acessar_graficos_glicemia
from gerar_graficos_glicemia import GraficosGlicemia


class AcessarGraficosGlicemia(QWidget, tela_acessar_graficos_glicemia.Ui_Form):
    def __init__(self, nome_documento_completo):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Gráficos - Glicemia')

        self.nome_documento_completo = nome_documento_completo

        self.app = QApplication([])

        self.graficos = GraficosGlicemia(self.nome_documento_completo)

        # Botão "A b r i r"
        self.abrir.clicked.connect(self.botao_abrir)

        # Botão "?"
        self.ajuda.clicked.connect(self.botao_ajuda)

    def botao_abrir(self):
        if self.media.isChecked():
            self.graficos.media_glicemia()
            self.graficos.show()
            self.app.exec_()

        elif self.desvio_padrao.isChecked():
            self.graficos.desvio_padrao_glicemia()
            self.graficos.show()
            self.app.exec_()

        elif self.variabilidade.isChecked():
            self.graficos.variabilidade_glicemia()
            self.graficos.show()
            self.app.exec_()

        elif self.massa.isChecked():
            self.graficos.massa_glicose()
            self.graficos.show()
            self.app.exec_()

        elif self.colher.isChecked():
            self.graficos.colher_cha_glicose()
            self.graficos.show()
            self.app.exec_()

        elif self.margem.isChecked():
            self.graficos.margem_glicemica_glicemia()
            self.graficos.show()
            self.app.exec_()

    def botao_ajuda(self):
        QMessageBox.information(
            self,
            'Ajuda - Gráficos Glicemia',
            '''Todos os gráficos são interativos e abertos em uma nova janela.
Somente um gráfico pode ser aberto por vez.

Média: Soma de todos os valores dividido pela quantidade de dados.

Desvio padrão: Informa o quão distante ou perto os valores estão da média.

Variabilidade: Informa a variação (em porcentagem) dos valores em relação a média. Quanto menor o valor, mas perto da média os valores estão.'''
        )
