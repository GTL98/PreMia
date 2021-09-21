from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from interface_grafica.interface_grafica_python import tela_acessar_banco_dados
from alimentar_glicemia import AdicionarDadosGlicemia
from alimentar_pressao import AdicionarDadosPressao
from alimentar_glicemia_pressao import AdicionarDadosGlicemiaPressao


class AcessarBancoDados(QWidget, tela_acessar_banco_dados.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Acessar Banco de Dados')

        self.adicionar_glicemia = AdicionarDadosGlicemia()
        self.adicionar_pressao = AdicionarDadosPressao()
        self.adicionar_glicemia_pressao = AdicionarDadosGlicemiaPressao()

        # Adicionar os itens do "combo_dia"
        dias_bd = list(range(1, 32))
        dias_str = [str(dia) for dia in dias_bd]
        self.combo_dia.addItems(dias_str)

        # Adicionar os itens do "combo_mes"
        meses_bd = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        self.combo_mes.addItems(meses_bd)

        # Adicionar os itens do "combo_ano"
        ano_atual = date.today().year
        anos_bd = list(range(1900, ano_atual+1))
        anos_str = [str(ano) for ano in anos_bd]
        self.combo_ano.addItems(anos_str)

        # Adicionar os itens do "combo_mes_bd"
        meses_bd = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        self.combo_mes_bd.addItems(meses_bd)

        # Adicionar os itens do "combo_ano_bd"
        ano_atual = date.today().year
        anos_bd = list(range(2019, ano_atual+1))
        anos_str = [str(ano) for ano in anos_bd]
        self.combo_ano_bd.addItems(anos_str)

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
                self.adicionar_glicemia.nome_documento_completo = nome_documento_completo
                self.adicionar_glicemia.show()
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
                self.adicionar_pressao.nome_documento_completo = nome_documento_completo
                self.adicionar_pressao.show()
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
                self.adicionar_glicemia_pressao.nome_documento_completo = nome_documento_completo
                self.adicionar_glicemia_pressao.show()
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
