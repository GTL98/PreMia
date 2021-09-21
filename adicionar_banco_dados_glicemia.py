from math import sqrt as raiz
from statistics import mean as media
from statistics import variance as var


def dados_glicemia_um_valor(nome_documento, dia, mes, ano, lista_peso, valores_glicemia):
    quantidade_dados = len(valores_glicemia)
    media_glicemia = valores_glicemia[0]
    desvio_padrao_glicemia = 0
    variabilidade_glicemia = 0

    peso_paciente = lista_peso[0]
    media_glicemia_convertida = media_glicemia / 100
    litros_sangue = 0.075 * peso_paciente
    massa_glicose = media_glicemia_convertida * litros_sangue
    colher_cha = massa_glicose / 4

    caminho = fr'banco_dados\{nome_documento}'

    with open(caminho, 'a') as doc:
        doc.write('\n')
        doc.write(f'{ano}-{mes}-{dia},{quantidade_dados},{media_glicemia},{desvio_padrao_glicemia},'
                  f'{variabilidade_glicemia},{massa_glicose:.1f},{colher_cha:.1f}')


def dados_glicemia_mais_valores(nome_documento, dia, mes, ano, lista_peso, valores_glicemia):
    quantidade_dados = len(valores_glicemia)
    media_glicemia = media(valores_glicemia)
    variancia_glicemia = var(valores_glicemia)
    desvio_padrao_glicemia = raiz(variancia_glicemia)
    variabilidade_glicemia = (desvio_padrao_glicemia / media_glicemia) * 100

    peso_paciente = lista_peso[0]
    media_glicemia_convertida = media_glicemia / 100
    litros_sangue = 0.075 * peso_paciente
    massa_glicose = media_glicemia_convertida * litros_sangue
    colher_cha = massa_glicose / 4

    caminho = fr'banco_dados\{nome_documento}'

    with open(caminho, 'a') as doc:
        doc.write('\n')
        doc.write(f'{ano}-{mes}-{dia},{quantidade_dados},{media_glicemia:.0f},{desvio_padrao_glicemia:.0f},'
                  f'{variabilidade_glicemia:.0f},{massa_glicose:.1f},{colher_cha:.1f}')
