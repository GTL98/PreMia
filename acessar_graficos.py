from datetime import date
from PyQt5.QtWidgets import QMessageBox, QWidget
from interface_grafica.interface_grafica_python import tela_acessar_graficos

from acessar_graficos_glicemia import AcessarGraficosGlicemia
from acessar_graficos_pressao import AcessarGraficosPressao
from acessar_graficos_glicemia_pressao import AcessarGraficosGlicemiaPressao


class AcessarGraficos(QWidget, tela_acessar_graficos.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Acessar Gráficos')

        # Adicionar itens ao "combo_dia"
        dias = list(range(1, 32))
        dias_str = [str(dia) for dia in dias]
        self.combo_dia.addItems(dias_str)

        # Adicionar itens ao "combo_mes"
        meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        self.combo_mes.addItems(meses)

        # Adicionar itens ao "combo_ano"
        ano_atual = date.today().year
        anos = list(range(1900, ano_atual+1))
        anos_str = [str(ano) for ano in anos]
        self.combo_ano.addItems(anos_str)

        # Adicionar itens ao "combo_mes_bd"
        meses_db = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        self.combo_mes_bd.addItems(meses_db)

        # Adicionar itens ao "combo_ano_bd"
        ano_atual = date.today().year
        anos_bd = list(range(2019, ano_atual+1))
        anos_str_bd = [str(ano_bd) for ano_bd in anos_bd]
        self.combo_ano_bd.addItems(anos_str_bd)

        # Botão "A c e s s a r"
        self.acessar.clicked.connect(self.botao_acessar)

        # Botão "?"
        self.ajuda.clicked.connect(self.botao_ajuda)

    def botao_acessar(self):
        if self.glicemia.isChecked():
            nome = self.linha_nome.text().upper().strip().split()
            nome_junto = '_'.join(nome)

            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()
            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            nome_documento_completo = f'{nome_junto}_{dia}_{mes}_{ano}_GLICEMIA_{mes_bd}_{ano_bd}.txt'
            caminho = fr'banco_dados\{nome_documento_completo}'

            try:
                with open(caminho) as doc:
                    doc.read()
            except FileNotFoundError:
                QMessageBox.warning(
                    self,
                    'Erro',
                    f'''O arquivo {nome_documento_completo} não foi encontrado.
Verifique novamente as informações colocadas.'''
                )
            else:
                self.acesso_graficos_glicemia = AcessarGraficosGlicemia(nome_documento_completo)
                self.acesso_graficos_glicemia.show()
                self.close()

        elif self.pressao.isChecked():
            nome = self.linha_nome.text().upper().strip().split()
            nome_junto = '_'.join(nome)

            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()
            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            nome_documento_completo = f'{nome_junto}_{dia}_{mes}_{ano}_PRESSAO_{mes_bd}_{ano_bd}.txt'
            caminho = fr'banco_dados\{nome_documento_completo}'

            try:
                with open(caminho) as doc:
                    doc.read()
            except FileNotFoundError:
                QMessageBox.warning(
                    self,
                    'Erro',
                    f'''O arquivo {nome_documento_completo} não foi encontrado.
Verifique novamente as informações colocadas.'''
                )
            else:
                self.acesso_graficos_pressao = AcessarGraficosPressao(nome_documento_completo)
                self.acesso_graficos_pressao.show()
                self.close()

        elif self.glicemia_pressao.isChecked():
            nome = self.linha_nome.text().upper().strip().split()
            nome_junto = '_'.join(nome)

            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()
            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            nome_documento_completo = f'{nome_junto}_{dia}_{mes}_{ano}_GLICEMIA_PRESSAO_{mes_bd}_{ano_bd}.txt'
            caminho = fr'banco_dados\{nome_documento_completo}'

            try:
                with open(caminho) as doc:
                    doc.read()
            except FileNotFoundError:
                QMessageBox.warning(
                    self,
                    'Erro',
                    f'''O arquivo {nome_documento_completo} não foi encontrado.
Verifique novamente as informações colocadas.'''
                )
            else:
                self.acesso_graficos_glicemia_pressao = AcessarGraficosGlicemiaPressao(nome_documento_completo)
                self.acesso_graficos_glicemia_pressao.show()
                self.close()

    def botao_ajuda(self):
        QMessageBox.information(
            self,
            'Ajuda',
            '''Nome: Indicar o nome completo do paciente.

Dia: Indicar o dia de nascimento do paciente.

Mês: Indicar o mês de nascimento do paciente.

Ano: Indicar o ano de nascimento do paciente.

Dentro da caixa "Banco de dados":

    Mês: Indicar o mês da medição.

    Ano: Indicar o ano da medição.

    Ao lado, selecionar um dos 3 tipos de medição.
'''
        )
