from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from interface_grafica.interface_grafica_python import tela_criar_banco_dados
from criar_documentos_banco_dados import Documentos


class CriarBancoDados(QWidget, tela_criar_banco_dados.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Criar Banco de Dados')

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

        # Botão "C r i a r"
        self.criar.clicked.connect(self.botao_criar)

        # Botão "V e r i f i c a r"
        self.verificar.clicked.connect(self.botao_verificar)

        # Botão "?"
        self.ajuda.clicked.connect(self.botao_ajuda)

    def botao_criar(self):
        if self.glicemia.isChecked():
            nome = self.linha_nome.text().upper().strip().split()
            nome_junto = '_'.join(nome)
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            nome_documento_completo = f'{nome_junto}_{dia}_{mes}_{ano}_GLICEMIA_{mes_bd}_{ano_bd}.txt'

            if 'GUILHERME_TREVISAN_LINHARES_1_MAI_1998' in nome_documento_completo:
                QMessageBox.information(
                    self,
                    'Easter Egg!',
                    'Parece que você encontrou o meu criador!'
                )
            else:
                documento = Documentos(nome_documento_completo)
                documento.banco_dados_glicemia(nome_documento_completo)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    f'O arquivo {nome_documento_completo} foi criado com sucesso!'
                )

        if self.pressao.isChecked():
            nome = self.linha_nome.text().upper().strip().split()
            nome_junto = '_'.join(nome)
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            nome_documento_completo = f'{nome_junto}_{dia}_{mes}_{ano}_PRESSAO_{mes_bd}_{ano_bd}.txt'

            if 'GUILHERME_TREVISAN_LINHARES_1_MAI_1998' in nome_documento_completo:
                QMessageBox.information(
                    self,
                    'Easter Egg!',
                    'Parece que você encontrou o meu criador!'
                )
            else:
                documento = Documentos(nome_documento_completo)
                documento.banco_dados_pressao(nome_documento_completo)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    f'O arquivo {nome_documento_completo} foi criado com sucesso!'
                )

        if self.glicemia_pressao.isChecked():
            nome = self.linha_nome.text().upper().strip().split()
            nome_junto = '_'.join(nome)
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            nome_documento_completo = f'{nome_junto}_{dia}_{mes}_{ano}_GLICEMIA_PRESSAO_{mes_bd}_{ano_bd}.txt'

            if 'GUILHERME_TREVISAN_LINHARES_1_MAI_1998' in nome_documento_completo:
                QMessageBox.information(
                    self,
                    'Easter Egg!',
                    'Parece que você encontrou o meu criador!'
                )
            else:
                documento = Documentos(nome_documento_completo)
                documento.banco_dados_glicemia_pressao(nome_documento_completo)
                QMessageBox.information(
                    self,
                    'Sucesso',
                    f'O arquivo {nome_documento_completo} foi criado com sucesso!'
                )

    def botao_verificar(self):

        if self.glicemia.isChecked():
            nome = self.linha_nome.text().upper().strip()
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            QMessageBox.information(
                self,
                'Verificar Informações',
                f'''Nome: {nome}
Dia do nascimento: {dia}
Mês do nascimento: {mes}
Ano do nascimento: {ano}
Tipo do banco de dados: GLICEMIA
Mês do Banco de dados: {mes_bd}
Ano do banco de dados: {ano_bd}'''
            )

        if self.pressao.isChecked():
            nome = self.linha_nome.text().upper().strip()
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            QMessageBox.information(
                self,
                'Verificar Informações',
                f'''Nome: {nome}
Dia do nascimento: {dia}
Mês do nascimento: {mes}
Ano do nascimento: {ano}
Tipo do banco de dados: PRESSÃO
Mês do Banco de dados: {mes_bd}
Ano do banco de dados: {ano_bd}'''
            )

        if self.glicemia_pressao.isChecked():
            nome = self.linha_nome.text().upper().strip()
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            mes_bd = self.combo_mes_bd.currentText()
            ano_bd = self.combo_ano_bd.currentText()

            QMessageBox.information(
                self,
                'Verificar Informações',
                f'''Nome: {nome}
Dia do nascimento: {dia}
Mês do nascimento: {mes}
Ano do nascimento: {ano}
Tipo do banco de dados: GLICEMIA + PRESSÃO
Mês do Banco de dados: {mes_bd}
Ano do banco de dados: {ano_bd}'''
            )

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
