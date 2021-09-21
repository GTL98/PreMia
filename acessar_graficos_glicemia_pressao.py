from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from interface_grafica.interface_grafica_python import tela_acessar_graficos_glicemia_pressao
from gerar_graficos_glicemia_pressao import GraficosGlicemiaPressao


class AcessarGraficosGlicemiaPressao(QWidget, tela_acessar_graficos_glicemia_pressao.Ui_Form):
    def __init__(self, nome_documento_completo):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Gráficos - Glicemia + Pressão')

        self.nome_documento_completo = nome_documento_completo

        self.app = QApplication([])

        self.graficos = GraficosGlicemiaPressao(self.nome_documento_completo)

        # Botão "A b r i r" da glicemia
        self.abrir_glicemia.clicked.connect(self.botao_abrir_glicemia)

        # Botão "A b r i r" da pressão
        self.abrir_pressao.clicked.connect(self.botao_abrir_pressao)

        # Botão "A b r i r" do BPM
        self.abrir_bpm.clicked.connect(self.botao_abrir_bpm)

        # Botão "?"
        self.ajuda.clicked.connect(self.botao_ajuda)

    def botao_abrir_glicemia(self):
        if self.media_glicemia.isChecked():
            self.graficos.media_glicemia()
            self.graficos.show()
            self.app.exec_()

        elif self.desvio_padrao_glicemia.isChecked():
            self.graficos.desvio_padrao_glicemia()
            self.graficos.show()
            self.app.exec_()

        elif self.variabilidade_glicemia.isChecked():
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

    def botao_abrir_pressao(self):
        if self.media_pressao.isChecked():
            self.graficos.media_pressao()
            self.graficos.show()
            self.app.exec_()

        elif self.desvio_padrao_pressao.isChecked():
            self.graficos.desvio_padrao_pressao()
            self.graficos.show()
            self.app.exec_()

        elif self.variabilidade_pressao.isChecked():
            self.graficos.variabilidade_pressao()
            self.graficos.show()
            self.app.exec_()

    def botao_abrir_bpm(self):
        if self.media_bpm.isChecked():
            self.graficos.media_bpm()
            self.graficos.show()
            self.app.exec_()

        elif self.desvio_padrao_bpm.isChecked():
            self.graficos.desvio_padrao_bpm()
            self.graficos.show()
            self.app.exec_()

        elif self.variabilidade_bpm.isChecked():
            self.graficos.variabilidade_bpm()
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
