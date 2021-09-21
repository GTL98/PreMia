from math import sqrt as raiz
from statistics import mean as media
from statistics import variance as var


def dados_pressao_um_valor(nome_documento, dia, mes, ano, valores_sistolica, valores_diastolica):
    quantidade_dados = len(valores_sistolica)

    media_sistolica = valores_sistolica[0]
    desvio_padrao_sistolica = 0
    variabilidade_sistolica = 0

    media_diastolica = valores_diastolica[0]
    desvio_padrao_diastolica = 0
    variabilidade_diastolica = 0

    caminho = fr'banco_dados\{nome_documento}'

    with open(caminho, 'a') as doc:
        doc.write('\n')
        doc.write(f'{ano}-{mes}-{dia},{quantidade_dados},{media_sistolica:.1f},{media_diastolica:.1f},'
                  f'{desvio_padrao_sistolica:.1f},{desvio_padrao_diastolica:.1f},{variabilidade_sistolica:.0f},'
                  f'{variabilidade_diastolica:.0f},')


def dados_pressao_mais_valores(nome_documento, dia, mes, ano, valores_sistolica, valores_diastolica):
    quantidade_dados = len(valores_sistolica)

    media_sistolica = media(valores_sistolica)
    variancia_sistolica = var(valores_sistolica)
    desvio_padrao_sistolica = raiz(variancia_sistolica)
    variabilidade_sistolica = (desvio_padrao_sistolica / media_sistolica) * 100

    media_diastolica = media(valores_diastolica)
    variancia_diastolica = var(valores_diastolica)
    desvio_padrao_diastolica = raiz(variancia_diastolica)
    variabilidade_diastolica = (desvio_padrao_diastolica / media_diastolica) * 100

    caminho = fr'banco_dados\{nome_documento}'

    with open(caminho, 'a') as doc:
        doc.write('\n')
        doc.write(f'{ano}-{mes}-{dia},{quantidade_dados},{media_sistolica:.1f},{media_diastolica:.1f},'
                  f'{desvio_padrao_sistolica:.1f},{desvio_padrao_diastolica:.1f},{variabilidade_sistolica:.0f},'
                  f'{variabilidade_diastolica:.0f},')


def dados_bpm_um_valor(nome_documento, valores_bpm):
    media_bpm = valores_bpm[0]
    desvio_padrao_bpm = 0
    variabilidade_bpm = 0

    caminho = fr'banco_dados\{nome_documento}'

    with open(caminho, 'a') as doc:
        doc.write(f'{media_bpm},{desvio_padrao_bpm},{variabilidade_bpm}')


def dados_bpm_mais_valores(nome_documento, valores_bpm):
    media_bpm = media(valores_bpm)
    variancia_bpm = var(valores_bpm)
    desvio_padrao_bpm = raiz(variancia_bpm)
    variabilidade_bpm = (desvio_padrao_bpm / media_bpm) * 100

    caminho = fr'banco_dados\{nome_documento}'

    with open(caminho, 'a') as doc:
        doc.write(f'{media_bpm:.0f},{desvio_padrao_bpm:.0f},{variabilidade_bpm:.0f}')
