from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from interface_grafica.interface_grafica_python import tela_adicionar_dados_glicemia
from adicionar_banco_dados_glicemia import (
    dados_glicemia_um_valor,
    dados_glicemia_mais_valores
)

valores_glicemia = []
lista_peso = []


class AdicionarDadosGlicemia(QWidget, tela_adicionar_dados_glicemia.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Alimentar Dados - Glicemia')

        self.nome_documento_completo = None

        # Adicionar os itens do "combo_dia"
        dias = list(range(1, 32))
        dias_str = [str(dia) for dia in dias]
        self.combo_dia.addItems(dias_str)

        # Adicionar os itens do "combo_mes"
        meses = list(range(1, 13))
        meses_str = [str(mes) for mes in meses]
        self.combo_mes.addItems(meses_str)

        # Adicionar os itens do "combo_ano"
        ano_atual = date.today().year
        anos = list(range(2019, ano_atual+1))
        anos_str = [str(ano) for ano in anos]
        self.combo_ano.addItems(anos_str)

        # Botão "A d i c i o n a r" da glicemia
        self.adicionar_glicemia.clicked.connect(self.botao_adicionar_glicemia)

        # Botão "E x c l u i r" da glicemia
        self.excluir_glicemia.clicked.connect(self.botao_excluir_glicemia)

        # Botão "A d i c i o n a r" do peso
        self.adicionar_peso.clicked.connect(self.botao_adicionar_peso)

        # Botão "E x c l u i r" do peso
        self.excluir_peso.clicked.connect(self.botao_excluir_peso)

        # Botão "?"
        self.ajuda.clicked.connect(self.botao_ajuda)

        # Botão "A d i c i o n a r" ao banco de dados
        self.adicionar_banco_dados.clicked.connect(self.botao_adicionar_banco_dados)

    def botao_adicionar_glicemia(self):
        try:
            glicemia = int(self.linha_glicemia.text())
        except ValueError:
            QMessageBox.warning(
                self,
                'Erro',
                'Digite números no campo "Valor da glicemia".'
            )
        else:
            glicemia_str = str(glicemia)

            if len(glicemia_str) > 3:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores no campo "Valores da glicemia" com até 3 dígitos.'
                )

            elif len(glicemia_str) < 2:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores no campo "Valores da glicemia" com mais de 1 dígito.'
                )

            elif glicemia <= 0:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores positivos no campo "Valores da glicemia".'
                )

            else:
                valores_glicemia.append(glicemia)
                self.linha_glicemia.setText('')
                self.lista_valores.addItem(glicemia_str)

    def botao_excluir_glicemia(self):
        for item in self.lista_valores.selectedItems():
            valor = int(item.text())
            indice = valores_glicemia.index(valor)
            del valores_glicemia[indice]
            self.lista_valores.takeItem(self.lista_valores.row(item))

    def botao_adicionar_peso(self):
        try:
            peso = int(self.linha_peso.text())
        except ValueError:
            QMessageBox.warning(
                self,
                'Erro',
                'Digite somente o valor do quilo no campo "Peso".'
            )
        else:
            peso_str = str(peso)

            if len(lista_peso) == 0:
                if len(peso_str) > 3:
                    QMessageBox.warning(
                        self,
                        'Erro',
                        'Digite o valor do peso com até 3 dígitos.'
                    )

                elif len(peso_str) < 2:
                    QMessageBox.warning(
                        self,
                        'Erro',
                        'Digite o valor do peso com mais de 1 dígito.'
                    )

                elif peso <= 0:
                    QMessageBox.warning(
                        self,
                        'Erro',
                        'Digite valores positivos para o peso.'
                    )

                else:
                    lista_peso.append(peso)
                    self.linha_peso.setText('')

            else:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Informar somente uma vez o peso do paciente no dia da medição.'
                )
                self.linha_peso.setText('')

    def botao_excluir_peso(self):
        del lista_peso[:]

    def botao_ajuda(self):
        QMessageBox.information(
            self,
            'Ajuda - Alimentar Dados - Glicemia',
            '''Dia: Informar o dia da medição.
            
Mês: Informar o mês da medição.

Ano: Informar o ano da medição.

Peso: Informar o peso do paciente no dia da medição. Aceita somente valores inteiros.

Valor da glicemia: Informar o valor da glicemia no dia da medição.'''
        )

    def botao_adicionar_banco_dados(self):
        if not valores_glicemia:
            QMessageBox.warning(
                self,
                'Erro',
                '''Os valores de GLICEMIA não foram informados.
Por favor, verifique se os dados informados estão na tela.'''
            )

        if not lista_peso:
            QMessageBox.warning(
                self,
                'Erro',
                '''O valor de PESO não foi informado.
Por favor, verifique se o dado foi adicionado.'''
            )

        if valores_glicemia and lista_peso:
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            if len(valores_glicemia) == 1:
                dados_glicemia_um_valor(self.nome_documento_completo, dia, mes, ano,
                                        lista_peso, valores_glicemia)

                del valores_glicemia[:]
                del lista_peso[:]

                self.lista_valores.clear()

                QMessageBox.information(
                    self,
                    'Dados enviados - Glicemia',
                    'Dados enviados ao banco de dados com sucesso!'
                )
            else:
                dados_glicemia_mais_valores(self.nome_documento_completo, dia, mes, ano,
                                            lista_peso, valores_glicemia)

                del valores_glicemia[:]
                del lista_peso[:]

                self.lista_valores.clear()

                QMessageBox.information(
                    self,
                    'Dados enviados - Glicemia',
                    'Dados enviados ao banco de dados com sucesso!'
                )
