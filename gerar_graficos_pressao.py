import csv
from datetime import datetime
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow
import plotly
from plotly.graph_objects import Figure, Scatter


class Graficosressao(QMainWindow):
    def __init__(self, nome_documento_completo):
        super().__init__()

        self.nome_documento_completo = nome_documento_completo
        self.caminho = fr'banco_dados\{self.nome_documento_completo}'

        self.lista_datas = []
        self.len_lista_datas = []

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
                self.lista_media_sistolica.append(float(row[2]))
                self.lista_media_diastolica.append(float(row[3]))
                self.lista_desvio_padrao_sistolica.append(float(row[4]))
                self.lista_desvio_padrao_diastolica.append(float(row[5]))
                self.lista_variabilidade_sistolica.append(int(row[6]))
                self.lista_variabilidade_diastolica.append(int(row[7]))
                self.lista_media_bpm.append(int(row[8]))
                self.lista_desvio_padrao_bpm.append(int(row[9]))
                self.lista_variabilidade_bpm.append(int(row[10]))

            for data in range(len(self.lista_datas)):
                self.len_lista_datas.append(data + 1)

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
