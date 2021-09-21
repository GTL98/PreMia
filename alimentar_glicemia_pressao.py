from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from interface_grafica.interface_grafica_python import tela_adicionar_dados_glicemia_pressao
from adicionar_banco_dados_glicemia_pressao import (
    dados_glicemia_um_valor,
    dados_glicemia_mais_valores,
    dados_pressao_um_valor,
    dados_pressao_mais_valores,
    dados_bpm_um_valor,
    dados_bpm_mais_valores
)

valores_glicemia = []
lista_peso = []
valores_sistolica = []
valores_diastolica = []
valores_bpm = []


class AdicionarDadosGlicemiaPressao(QWidget, tela_adicionar_dados_glicemia_pressao.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Alimentar Dados - Glicemia + Pressão')

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

        # Botão "A d i c i o n a r" do peso
        self.adicionar_peso.clicked.connect(self.botao_adicionar_peso)

        # Botão "E x c l u i r" do peso
        self.excluir_peso.clicked.connect(self.botao_excluir_peso)

        # Botão "A d i c i o n a r" da glicemia
        self.adicionar_glicemia.clicked.connect(self.botao_adicionar_glicemia)

        # Botão "E x c l u i r" da glicemia
        self.excluir_glicemia.clicked.connect(self.botao_excluir_glicemia)

        # Botão "A d i c i o n a r" da sistólica
        self.adicionar_sistolica.clicked.connect(self.botao_adicionar_sistolica)

        # Botão "E x c l u i r" da sistólica
        self.excluir_sistolica.clicked.connect(self.botao_excluir_sistolica)

        # Botão "A d i c i o n a r" da diastólica
        self.adicionar_diastolica.clicked.connect(self.botao_adicionar_diastolica)

        # Botão "E x c l u i r" da diastólica
        self.excluir_diastolica.clicked.connect(self.botao_excluir_diastolica)

        # Botão "A d i c i o n a r" do BPM
        self.adicionar_bpm.clicked.connect(self.botao_adicionar_bpm)

        # Botão "E x c l u i r" do BPM
        self.excluir_bpm.clicked.connect(self.botao_excluir_bpm)

        # Botão "?"
        self.ajuda.clicked.connect(self.botao_ajuda)

        # Botão "A d i c i o n a r" do banco de dados
        self.adicionar_banco_dados.clicked.connect(self.botao_adicionar_banco_dados)

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
                self.lista_glicemia.addItem(glicemia_str)

    def botao_excluir_glicemia(self):
        for item in self.lista_glicemia.selectedItems():
            valor = int(item.text())
            indice = valores_glicemia.index(valor)
            del valores_glicemia[indice]
            self.lista_glicemia.takeItem(self.lista_glicemia.row(item))

    def botao_adicionar_sistolica(self):
        try:
            sistolica = int(self.linha_sistolica.text())
            sistolica_float = sistolica / 10
        except ValueError:
            QMessageBox.warning(
                self,
                'Erro',
                '''Digite os valores de "Pressão Sistólica" sem o uso de ponto ou vírgula.
Digite o valor de forma inteira.
Por exemplo: 12,8 ou 12.8 como 128.'''
            )
        else:
            sistolica_str = str(sistolica_float)
            sistolica_int_str = str(sistolica)

            if len(sistolica_int_str) > 3:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores de PRESSSÃO SISTÓLICA com no máximo 3 dígitos.'
                )

            elif len(sistolica_int_str) < 2:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores de PRESSÃO SISTÓLICA com mais de 1 dígito.'
                )

            elif sistolica <= 0:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores positivos para PRESSÃO SISTÓLICA.'
                )
            else:
                valores_sistolica.append(sistolica_float)
                self.linha_sistolica.setText('')
                self.lista_sistolica.addItem(sistolica_str)
            
    def botao_excluir_sistolica(self):
        for item in self.lista_sistolica.selectedItems():
            valor = float(item.text())
            indice = valores_sistolica.index(valor)
            del valores_sistolica[indice]
            self.lista_sistolica.takeItem(self.lista_sistolica.row(item))

    def botao_adicionar_diastolica(self):
        try:
            diastolica = int(self.linha_diastolica.text())
            diastolica_float = diastolica / 10
        except ValueError:
            QMessageBox.warning(
                self,
                'Erro',
                '''Digite os valores de "Pressão Diastólica" sem o uso de ponto ou vírgula.
Digite o valor de forma inteira.
Por exemplo: 8,4 ou 8.4 como 84.'''
            )
        else:
            diastolica_str = str(diastolica_float)
            diastolica_int_str = str(diastolica)

            if len(diastolica_int_str) > 3:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores de PRESSSÃO DIASTÓLICA com no máximo 3 dígitos.'
                )

            elif len(diastolica_int_str) < 2:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores de PRESSÃO DIASTÓLICA com mais de 1 dígito.'
                )

            elif diastolica <= 0:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores positivos para PRESSÃO DIASTÓLICA.'
                )
            else:
                valores_diastolica.append(diastolica_float)
                self.linha_diastolica.setText('')
                self.lista_diastolica.addItem(diastolica_str)

    def botao_excluir_diastolica(self):
        for item in self.lista_diastolica.selectedItems():
            valor = float(item.text())
            indice = valores_diastolica.index(valor)
            del valores_diastolica[indice]
            self.lista_diastolica.takeItem(self.lista_diastolica.row(item))

    def botao_adicionar_bpm(self):
        try:
            bpm = int(self.linha_bpm.text())
        except ValueError:
            QMessageBox.warning(
                self,
                'Erro',
                'Digite números no campo "BPM".'
            )
        else:
            bpm_str = str(bpm)
            if len(bpm_str) > 3:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores de BPM com no máximo 3 dígitos.'
                )

            elif len(bpm_str) < 2:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores de BPM com mais de 1 dígito.'
                )

            elif bpm <= 0:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'Digite valores positivos para BPM.'
                )

            elif bpm > 220:
                QMessageBox.warning(
                    self,
                    'Erro',
                    'O valor máximo de BPM é de 220.'
                )

            else:
                valores_bpm.append(bpm)
                self.linha_bpm.setText('')
                self.lista_bpm.addItem(bpm_str)

    def botao_excluir_bpm(self):
        for item in self.lista_bpm.selectedItems():
            valor = int(item.text())
            indice = valores_bpm.index(valor)
            del valores_bpm[indice]
            self.lista_bpm.takeItem(self.lista_bpm.row(item))

    def botao_ajuda(self):
        QMessageBox.information(
            self,
            'Ajuda - Alimentar Dados - Glicemia + Pressão',
            '''Dia: Informar o dia da medição.
    
Mês: Informar o mês da medição.

Ano: Informar o ano da medição.

Peso: Informar o peso do paciente no dia da medição. Aceita somente valores inteiros.

Valor da glicemia: Informar o valor da glicemia no dia da medição.

Os valores de pressão (sistólica e diastólica) devem ser informados sem o uso de ponto ou vírgula.'''
        )

    def botao_adicionar_banco_dados(self):
        if not lista_peso:
            QMessageBox.warning(
                self,
                'Erro',
                '''O valor de PESO não foi informado.
Por favor, verifique se o dado foi adicionado.'''
            )

        if not valores_glicemia:
            QMessageBox.warning(
                self,
                'Erro',
                '''Os valores de GLICEMIA não foram informados.
Por favor, verifique se os dados informados estão na tela.'''
            )

        if not valores_sistolica:
            QMessageBox.warning(
                self,
                'Erro',
                '''Os valores da PRESSÃO SISTÓLICA não foram informados.
Por favor, verifique se os dados informados estão na tela.'''
            )

        if not valores_diastolica:
            QMessageBox.warning(
                self,
                'Erro',
                '''Os valores da PRESSÃO DIASTÓLICA não foram informados.
Por favor, verifique se os dados informados estão na tela.'''
            )

        if not valores_bpm:
            QMessageBox.warning(
                self,
                'Erro',
                '''Os valores do BPM não foram informados.
Por favor, verifique se os dados informados estão na tela.'''
            )

        if len(valores_sistolica) != len(valores_diastolica):
            QMessageBox.warning(
                self,
                'Erro',
                '''A quantidade de valores da PRESSÃO SISTÓLICA e PRESSÃO DIASTÓLICA estão diferentes.
Por favor, verifique a quantidade de dados informado na tela.'''
            )

        if (lista_peso and valores_glicemia and valores_sistolica and valores_diastolica and valores_bpm
                and (len(valores_sistolica) == len(valores_diastolica))):
            dia = self.combo_dia.currentText()
            mes = self.combo_mes.currentText()
            ano = self.combo_ano.currentText()

            if (len(valores_glicemia) and len(valores_sistolica)) == 1:
                dados_glicemia_um_valor(self.nome_documento_completo, dia, mes, ano,
                                        lista_peso, valores_glicemia)
                dados_pressao_um_valor(self.nome_documento_completo, valores_sistolica,
                                       valores_diastolica)
                dados_bpm_um_valor(self.nome_documento_completo, valores_bpm)

                del valores_glicemia[:]
                del lista_peso[:]
                del valores_sistolica[:]
                del valores_diastolica[:]
                del valores_bpm[:]
                self.lista_glicemia.clear()
                self.lista_sistolica.clear()
                self.lista_diastolica.clear()
                self.lista_bpm.clear()

                QMessageBox.information(
                    self,
                    'Dados enviados - Glicemia + Pressão',
                    'Dados enviados ao banco de dados com sucesso!'
                )

            elif (len(valores_glicemia) == 1) and (len(valores_sistolica) > 1):
                dados_glicemia_um_valor(self.nome_documento_completo, dia, mes, ano,
                                        lista_peso, valores_glicemia)
                dados_pressao_mais_valores(self.nome_documento_completo, valores_sistolica,
                                           valores_diastolica)
                dados_bpm_mais_valores(self.nome_documento_completo, valores_bpm)

                del valores_glicemia[:]
                del lista_peso[:]
                del valores_sistolica[:]
                del valores_diastolica[:]
                del valores_bpm[:]

                self.lista_glicemia.clear()
                self.lista_sistolica.clear()
                self.lista_diastolica.clear()
                self.lista_bpm.clear()

                QMessageBox.information(
                    self,
                    'Dados enviados - Glicemia + Pressão',
                    'Dados enviados ao banco de dados com sucesso!'
                )

            elif (len(valores_glicemia) > 1) and (len(valores_sistolica) == 1):
                dados_glicemia_mais_valores(self.nome_documento_completo, dia, mes, ano,
                                            lista_peso, valores_glicemia)
                dados_pressao_um_valor(self.nome_documento_completo, valores_sistolica,
                                       valores_diastolica)
                dados_bpm_um_valor(self.nome_documento_completo, valores_bpm)

                del valores_glicemia[:]
                del lista_peso[:]
                del valores_sistolica[:]
                del valores_diastolica[:]
                del valores_bpm[:]

                self.lista_glicemia.clear()
                self.lista_sistolica.clear()
                self.lista_diastolica.clear()
                self.lista_bpm.clear()

                QMessageBox.information(
                    self,
                    'Dados enviados - Glicemia + Pressão',
                    'Dados enviados ao banco de dados com sucesso!'
                )

            else:
                dados_glicemia_mais_valores(self.nome_documento_completo, dia, mes, ano,
                                            lista_peso, valores_glicemia)
                dados_pressao_mais_valores(self.nome_documento_completo, valores_sistolica,
                                           valores_diastolica)
                dados_bpm_mais_valores(self.nome_documento_completo, valores_bpm)

                del valores_glicemia[:]
                del lista_peso[:]
                del valores_sistolica[:]
                del valores_diastolica[:]
                del valores_bpm[:]

                self.lista_glicemia.clear()
                self.lista_sistolica.clear()
                self.lista_diastolica.clear()
                self.lista_bpm.clear()

                QMessageBox.information(
                    self,
                    'Dados enviados - Glicemia + Pressão',
                    'Dados enviados ao banco de dados com sucesso!'
                )
