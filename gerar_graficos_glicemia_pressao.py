import csv
from datetime import datetime
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow
import plotly
from plotly.graph_objects import Figure, Scatter


class GraficosGlicemiaPressao(QMainWindow):
    def __init__(self, nome_documento_completo):
        super().__init__()

        self.nome_documento_completo = nome_documento_completo
        self.caminho = fr'banco_dados\{self.nome_documento_completo}'

        self.lista_datas = []
        self.len_lista_datas = []

        self.lista_media_glicemia = []
        self.lista_maximo_glicemia = []
        self.lista_minimo_glicemia = []

        self.lista_desvio_padrao_glicemia = []
        self.lista_maximo_desvio_padrao_glicemia = []

        self.lista_variabilidade_glicemia = []
        self.lista_maximo_variabilidade_glicemia = []

        self.lista_massa_glicose = []
        self.lista_colher_cha = []

        self.lista_media_sistolica = []
        self.lista_media_diastolica = []

        self.lista_desvio_padrao_sistolica = []
        self.lista_desvio_padrao_diastolica = []

        self.lista_variabilidade_sistolica = []
        self.lista_variabilidade_diastolica = []

        self.lista_media_bpm = []
        self.lista_desvio_padrao_bpm = []
        self.lista_variabilidade_bpm = []

        with open(self.caminho) as doc:
            reader = csv.reader(doc)
            header_row = next(reader)

            for row in reader:
                datas = datetime.strptime(row[0], '%Y-%m-%d')
                self.lista_datas.append(datas)
                self.lista_media_glicemia.append(int(row[2]))
                self.lista_maximo_glicemia.append(180)
                self.lista_minimo_glicemia.append(70)
                self.lista_desvio_padrao_glicemia.append(int(row[3]))
                self.lista_maximo_desvio_padrao_glicemia.append(50)
                self.lista_variabilidade_glicemia.append(int(row[4]))
                self.lista_maximo_variabilidade_glicemia.append(36)
                self.lista_massa_glicose.append(float(row[5]))
                self.lista_colher_cha.append(float(row[6]))
                self.lista_media_sistolica.append(float(row[8]))
                self.lista_media_diastolica.append(float(row[9]))
                self.lista_desvio_padrao_sistolica.append(float(row[10]))
                self.lista_desvio_padrao_diastolica.append(float(row[11]))
                self.lista_variabilidade_sistolica.append(int(row[12]))
                self.lista_variabilidade_diastolica.append(int(row[13]))
                self.lista_media_bpm.append(int(row[14]))
                self.lista_desvio_padrao_bpm.append(int(row[15]))
                self.lista_variabilidade_bpm.append(int(row[16]))

            for data in range(len(self.lista_datas)):
                self.len_lista_datas.append(data + 1)

    def media_glicemia(self):
        self.setWindowTitle('Média - Glicemia')

        x = self.len_lista_datas
        y = self.lista_media_glicemia

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Média Glicemia (mg/dL)',
            marker=dict(
                color='green'
            )
        ))

        fig.update_layout(
            title=f'Média Glicemia (mg/dL) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Média Glicemia (mg/dL)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def desvio_padrao_glicemia(self):
        self.setWindowTitle('Desvio Padrão - Glicemia')

        x = self.len_lista_datas
        y = self.lista_desvio_padrao_glicemia
        y_maximo = self.lista_maximo_desvio_padrao_glicemia

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Desvio Padrão (mg/dL)',
            marker=dict(
                color='green'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y_maximo,
            name='Máximo (50 mg/dL)',
            marker=dict(
                color='red'
            )
        ))

        fig.update_layout(
            title=f'Desvio Padrão Glicemia (mg/dL) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Desvio Padrão (mg/dL)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def variabilidade_glicemia(self):
        self.setWindowTitle('Variabilidade - Glicemia')

        x = self.len_lista_datas
        y = self.lista_variabilidade_glicemia
        y_maximo = self.lista_maximo_variabilidade_glicemia

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Variabilidade (%)',
            marker=dict(
                color='green'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y_maximo,
            name='Máximo (36%)',
            marker=dict(
                color='red'
            )
        ))

        fig.update_layout(
            title=f'Variabilidade Glicemia (%) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Variabilidade (%)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def massa_glicose(self):
        self.setWindowTitle('Massa Glicose')

        x = self.len_lista_datas
        y = self.lista_massa_glicose

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Massa Glicose (g)',
            marker=dict(
                color='green'
            )
        ))

        fig.update_layout(
            title=f'Massa Glicose (g) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Massa Glicose (g)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def colher_cha_glicose(self):
        self.setWindowTitle('Colher de Chá')

        x = self.len_lista_datas
        y = self.lista_colher_cha

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Colher de Chá',
            marker=dict(
                color='green'
            )
        ))

        fig.update_layout(
            title=f'Colher de Chá - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Colher de Chá',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def margem_glicemica_glicemia(self):
        self.setWindowTitle('Margem Glicêmica')

        x = self.len_lista_datas
        y = self.lista_media_glicemia
        y_maximo = self.lista_maximo_glicemia
        y_minimo = self.lista_minimo_glicemia

        valores_intervalo = []
        y_porcentagem = [75]
        x_porcentagem = []

        for valor in y:
            if 70 <= valor <= 180:
                valores_intervalo.append(valor)

        porcentagem = int(len(valores_intervalo) / len(x) * 100)

        x_porcentagem.append(int(len(x)/2))

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y_maximo,
            name='Máximo (180 mg/dL)',
            marker=dict(
                color='red'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Média Glicemia (mg/dL)',
            marker=dict(
                color='green'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y_minimo,
            name='Mínimo (70 mg/dL)',
            marker=dict(
                color='blue'
            )
        ))

        fig.add_trace(Scatter(
            x=x_porcentagem,
            y=y_porcentagem,
            name=f'{porcentagem}% dos valores no intervalo',
            marker=dict(
                color='#ffffff'
            )
        ))

        fig.update_layout(
            title=f'Margem Glicêmica (mg/dL) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Margem Glicêmica (mg/dL)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def media_pressao(self):
        self.setWindowTitle('Média - Pressão')

        x = self.len_lista_datas
        y_sis = self.lista_media_sistolica
        y_dia = self.lista_media_diastolica

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y_sis,
            name='Sistólica (mmHg)',
            marker=dict(
                color='red'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y_dia,
            name='Diastólica (mmHg)',
            marker=dict(
                color='blue'
            )
        ))

        fig.update_layout(
            title=f'Média Pressão Arterial (mmHg) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Pressão Arterial (mmHg)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def desvio_padrao_pressao(self):
        self.setWindowTitle('Desvio Padrão - Pressão')

        x = self.len_lista_datas
        y_sis = self.lista_desvio_padrao_sistolica
        y_dia = self.lista_desvio_padrao_diastolica

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y_sis,
            name='Sistólica (mmHg)',
            marker=dict(
                color='red'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y_dia,
            name='Diastólica (mmHg)',
            marker=dict(
                color='blue'
            )
        ))

        fig.update_layout(
            title=f'Desvio Padrão Pressão Arterial (mmHg) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Desvio Padrão (mmHg)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def variabilidade_pressao(self):
        self.setWindowTitle('Variabilidade - Pressão')

        x = self.len_lista_datas
        y_sis = self.lista_variabilidade_sistolica
        y_dia = self.lista_variabilidade_diastolica

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y_sis,
            name='Sistólica (%)',
            marker=dict(
                color='red'
            )
        ))

        fig.add_trace(Scatter(
            x=x,
            y=y_dia,
            name='Diastólica (%)',
            marker=dict(
                color='blue'
            )
        ))

        fig.update_layout(
            title=f'Variabilidade Pressão Arterial (%) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Variabilidade (%)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def media_bpm(self):
        self.setWindowTitle('Média - BPM')

        x = self.len_lista_datas
        y = self.lista_media_bpm

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Média Frequência Cardíaca (BPM)',
            marker=dict(
                color='red'
            )
        ))

        fig.update_layout(
            title=f'Média Frequência Cardíaca (BPM) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Média (BPM)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def desvio_padrao_bpm(self):
        self.setWindowTitle('Desvio Padrão - BPM')

        x = self.len_lista_datas
        y = self.lista_desvio_padrao_bpm

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Desvio Padrão Frequência Cardíaca (BPM)',
            marker=dict(
                color='red'
            )
        ))

        fig.update_layout(
            title=f'Desvio Padrão Frequência Cardíaca (BPM) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Desvio Padrão (BPM)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

    def variabilidade_bpm(self):
        self.setWindowTitle('Variabilidade - BPM')

        x = self.len_lista_datas
        y = self.lista_variabilidade_bpm

        fig = Figure()

        fig.add_trace(Scatter(
            x=x,
            y=y,
            name='Variabilidade Frequência Cardíaca (%)',
            marker=dict(
                color='red'
            )
        ))

        fig.update_layout(
            title=f'Variabilidade Frequência Cardíaca (%) - {self.nome_documento_completo[-12:-9]}/'
                  f'{self.nome_documento_completo[-8:-4]}',
            xaxis_title='Dias',
            yaxis_title='Variabilidade (%)',
            font=dict(
                size=18
            )
        )

        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)
