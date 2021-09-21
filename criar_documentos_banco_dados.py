class Documentos:
    def __init__(self, nome_documento_completo):
        self.nome_documento_completo = nome_documento_completo

    def banco_dados_glicemia(self, nome_documento_completo):
        caminho = fr'banco_dados\{nome_documento_completo}'
        with open(caminho, 'w') as doc:
            doc.write('0_DATA,1_DADOS,2_MEDIA,3_DESVIO_PADRAO,4_VARIABILIDADE,5_MASSA_GLICOSE,6_COLHER_CHA')

    def banco_dados_pressao(self, nome_documento_junto):
        caminho = fr'banco_dados\{nome_documento_junto}'
        with open(caminho, 'w') as doc:
            doc.write('0_DATA,1_DADOS,2_MEDIA_SIS,3_MEDIA_DIA,4_DESVIO_PADRAO_SIS,5_DESVIO_PADRAO_DIA,'
                      '6_VARIABILIDADE_SIS,7_VARIABILIDADE_DIA,8_MEDIA_BPM,9_DESVIO_PADRAO_BPM,'
                      '10_VARIABILIDADE_BPM')

    def banco_dados_glicemia_pressao(self, nome_documento_junto):
        caminho = fr'banco_dados\{nome_documento_junto}'
        with open(caminho, 'w') as doc:
            doc.write('0_DATA,1_DADOS_GLICEMIA,2_MEDIA_GLICEMIA,3_DESVIO_PADRAO_GLICEMIA,'
                      '4_VARIABILIDADE_GLICEMIA,5_MASSA_GLICOSE,6_COLHER_CHA,7_DADOS_PRESSAO,8_MEDIA_SIS,'
                      '9_MEDIA_DIA,10_DESVIO_PADRAO_SIS,11_DESVIO_PADRAO_DIA,12_VARIABILIDADE_SIS,'
                      '13_VARIABILIDADE_DIA,14_MEDIA_BPM,15_DESVIO_PADRAO_BPM,16_VARIABILIDADE_BPM')