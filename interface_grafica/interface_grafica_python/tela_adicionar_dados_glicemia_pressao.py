# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_adicionar_dados_glicemia_pressao.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(770, 550)
        Form.setMinimumSize(QtCore.QSize(770, 550))
        Form.setMaximumSize(QtCore.QSize(770, 550))
        Form.setStyleSheet("QPushButton#adicionar_peso, #excluir_peso, #adicionar_glicemia, #excluir_glicemia, #adicionar_sistolica, #excluir_sistolica, #adicionar_diastolica, #excluir_diastolica,\n"
"#adicionar_bpm, #excluir_bpm, #adicionar_banco_dados{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px\n"
"}\n"
"QPushButton#adicionar_peso:hover, #excluir_peso:hover, #adicionar_glicemia:hover, #excluir_glicemia:hover, #adicionar_sistolica:hover, #excluir_sistolica:hover, #adicionar_diastolica:hover, #excluir_diastolica:hover, #adicionar_bpm:hover, #excluir_bpm:hover, #adicionar_banco_dados:hover{\n"
"background-color: rgba(145, 207, 230, 200)\n"
"}\n"
"QPushButton#adicionar_peso:pressed, #excluir_peso:pressed, #adicionar_glicemia:pressed, #excluir_glicemia:pressed, #adicionar_sistolica:pressed, #excluir_sistolica:pressed, #adicionar_diastolica:pressed, #excluir_diastolica:pressed, #adicionar_bpm:pressed, #excluir_bpm:pressed, #adicionar_banco_dados:pressed{\n"
"background-color: rgba(150, 150, 150, 255);\n"
"padding-top: 2px;\n"
"}\n"
"\n"
"QLineEdit#linha_peso, #linha_glicemia, #linha_sistolica, #linha_diastolica, #linha_bpm{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(0, 0, 0)\n"
"}\n"
"QLineEdit#linha_peso:hover, #linha_glicemia:hover, #linha_sistolica:hover, #linha_diastolica:hover, #linha_bpm:hover{\n"
"background-color: rgba(147, 207, 230, 100)\n"
"}\n"
"\n"
"QComboBox#combo_dia, #combo_mes, #combo_ano{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px\n"
"}\n"
"QComboBox#combo_dia:hover, #combo_mes:hover, #combo_ano:hover{\n"
"background-color: rgba(147, 207, 230, 200)\n"
"}")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.ajuda = QtWidgets.QPushButton(Form)
        self.ajuda.setMinimumSize(QtCore.QSize(30, 30))
        self.ajuda.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ajuda.setFont(font)
        self.ajuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ajuda.setStyleSheet("QPushButton#ajuda{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-radius: 10px\n"
"}\n"
"QPushButton#ajuda:hover{\n"
"background-color: rgba(145, 207, 230, 200)\n"
"}\n"
"QPushButton#ajuda:pressed{\n"
"padding-top: 2px\n"
"}\n"
"")
        self.ajuda.setObjectName("ajuda")
        self.horizontalLayout_7.addWidget(self.ajuda)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.combo_dia = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_dia.setFont(font)
        self.combo_dia.setObjectName("combo_dia")
        self.horizontalLayout_8.addWidget(self.combo_dia)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.combo_mes = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_mes.setFont(font)
        self.combo_mes.setObjectName("combo_mes")
        self.horizontalLayout_9.addWidget(self.combo_mes)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.combo_ano = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_ano.setFont(font)
        self.combo_ano.setObjectName("combo_ano")
        self.horizontalLayout_11.addWidget(self.combo_ano)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.lista_glicemia = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lista_glicemia.setFont(font)
        self.lista_glicemia.setObjectName("lista_glicemia")
        self.verticalLayout.addWidget(self.lista_glicemia)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.linha_peso = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linha_peso.setFont(font)
        self.linha_peso.setObjectName("linha_peso")
        self.verticalLayout_9.addWidget(self.linha_peso)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.adicionar_peso = QtWidgets.QPushButton(Form)
        self.adicionar_peso.setMinimumSize(QtCore.QSize(80, 40))
        self.adicionar_peso.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar_peso.setFont(font)
        self.adicionar_peso.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adicionar_peso.setObjectName("adicionar_peso")
        self.horizontalLayout_5.addWidget(self.adicionar_peso, 0, QtCore.Qt.AlignLeft)
        self.excluir_peso = QtWidgets.QPushButton(Form)
        self.excluir_peso.setMinimumSize(QtCore.QSize(80, 40))
        self.excluir_peso.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.excluir_peso.setFont(font)
        self.excluir_peso.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_peso.setObjectName("excluir_peso")
        self.horizontalLayout_5.addWidget(self.excluir_peso, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.linha_glicemia = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linha_glicemia.setFont(font)
        self.linha_glicemia.setObjectName("linha_glicemia")
        self.verticalLayout_5.addWidget(self.linha_glicemia)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adicionar_glicemia = QtWidgets.QPushButton(Form)
        self.adicionar_glicemia.setMinimumSize(QtCore.QSize(80, 40))
        self.adicionar_glicemia.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar_glicemia.setFont(font)
        self.adicionar_glicemia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adicionar_glicemia.setObjectName("adicionar_glicemia")
        self.horizontalLayout.addWidget(self.adicionar_glicemia, 0, QtCore.Qt.AlignLeft)
        self.excluir_glicemia = QtWidgets.QPushButton(Form)
        self.excluir_glicemia.setMinimumSize(QtCore.QSize(80, 40))
        self.excluir_glicemia.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.excluir_glicemia.setFont(font)
        self.excluir_glicemia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_glicemia.setObjectName("excluir_glicemia")
        self.horizontalLayout.addWidget(self.excluir_glicemia, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.lista_sistolica = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lista_sistolica.setFont(font)
        self.lista_sistolica.setObjectName("lista_sistolica")
        self.verticalLayout_2.addWidget(self.lista_sistolica)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.linha_sistolica = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linha_sistolica.setFont(font)
        self.linha_sistolica.setObjectName("linha_sistolica")
        self.verticalLayout_6.addWidget(self.linha_sistolica)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.adicionar_sistolica = QtWidgets.QPushButton(Form)
        self.adicionar_sistolica.setMinimumSize(QtCore.QSize(80, 40))
        self.adicionar_sistolica.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar_sistolica.setFont(font)
        self.adicionar_sistolica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adicionar_sistolica.setObjectName("adicionar_sistolica")
        self.horizontalLayout_2.addWidget(self.adicionar_sistolica, 0, QtCore.Qt.AlignLeft)
        self.excluir_sistolica = QtWidgets.QPushButton(Form)
        self.excluir_sistolica.setMinimumSize(QtCore.QSize(80, 40))
        self.excluir_sistolica.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.excluir_sistolica.setFont(font)
        self.excluir_sistolica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_sistolica.setObjectName("excluir_sistolica")
        self.horizontalLayout_2.addWidget(self.excluir_sistolica, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.lista_diastolica = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lista_diastolica.setFont(font)
        self.lista_diastolica.setObjectName("lista_diastolica")
        self.verticalLayout_3.addWidget(self.lista_diastolica)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.linha_diastolica = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linha_diastolica.setFont(font)
        self.linha_diastolica.setObjectName("linha_diastolica")
        self.verticalLayout_7.addWidget(self.linha_diastolica)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.adicionar_diastolica = QtWidgets.QPushButton(Form)
        self.adicionar_diastolica.setMinimumSize(QtCore.QSize(80, 40))
        self.adicionar_diastolica.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar_diastolica.setFont(font)
        self.adicionar_diastolica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adicionar_diastolica.setObjectName("adicionar_diastolica")
        self.horizontalLayout_3.addWidget(self.adicionar_diastolica, 0, QtCore.Qt.AlignLeft)
        self.excluir_diastolica = QtWidgets.QPushButton(Form)
        self.excluir_diastolica.setMinimumSize(QtCore.QSize(80, 40))
        self.excluir_diastolica.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.excluir_diastolica.setFont(font)
        self.excluir_diastolica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_diastolica.setObjectName("excluir_diastolica")
        self.horizontalLayout_3.addWidget(self.excluir_diastolica, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.lista_bpm = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lista_bpm.setFont(font)
        self.lista_bpm.setObjectName("lista_bpm")
        self.verticalLayout_4.addWidget(self.lista_bpm)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.linha_bpm = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linha_bpm.setFont(font)
        self.linha_bpm.setObjectName("linha_bpm")
        self.verticalLayout_8.addWidget(self.linha_bpm)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.adicionar_bpm = QtWidgets.QPushButton(Form)
        self.adicionar_bpm.setMinimumSize(QtCore.QSize(80, 40))
        self.adicionar_bpm.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar_bpm.setFont(font)
        self.adicionar_bpm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adicionar_bpm.setObjectName("adicionar_bpm")
        self.horizontalLayout_4.addWidget(self.adicionar_bpm, 0, QtCore.Qt.AlignLeft)
        self.excluir_bpm = QtWidgets.QPushButton(Form)
        self.excluir_bpm.setMinimumSize(QtCore.QSize(80, 40))
        self.excluir_bpm.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.excluir_bpm.setFont(font)
        self.excluir_bpm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_bpm.setObjectName("excluir_bpm")
        self.horizontalLayout_4.addWidget(self.excluir_bpm, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.adicionar_banco_dados = QtWidgets.QPushButton(Form)
        self.adicionar_banco_dados.setMinimumSize(QtCore.QSize(120, 60))
        self.adicionar_banco_dados.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar_banco_dados.setFont(font)
        self.adicionar_banco_dados.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adicionar_banco_dados.setObjectName("adicionar_banco_dados")
        self.verticalLayout_10.addWidget(self.adicionar_banco_dados, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Alimentar Banco de dados Glicemia + Pressão"))
        self.ajuda.setText(_translate("Form", "?"))
        self.label_8.setText(_translate("Form", "Dia:"))
        self.label_9.setText(_translate("Form", "Mês:"))
        self.label_10.setText(_translate("Form", "Ano:"))
        self.label_2.setText(_translate("Form", "Glicemia"))
        self.label_6.setText(_translate("Form", "Peso:"))
        self.adicionar_peso.setText(_translate("Form", "A d i c i o n a r"))
        self.excluir_peso.setText(_translate("Form", "E x c l u i r"))
        self.label_7.setText(_translate("Form", "Valor da glicemia:"))
        self.adicionar_glicemia.setText(_translate("Form", "A d i c i o n a r"))
        self.excluir_glicemia.setText(_translate("Form", "E x c l u i r"))
        self.label_5.setText(_translate("Form", "Pressão Sistólica"))
        self.adicionar_sistolica.setText(_translate("Form", "A d i c i o n a r"))
        self.excluir_sistolica.setText(_translate("Form", "E x c l u i r"))
        self.label_4.setText(_translate("Form", "Pressão Diastólica"))
        self.adicionar_diastolica.setText(_translate("Form", "A d i c i o n a r"))
        self.excluir_diastolica.setText(_translate("Form", "E x c l u i r"))
        self.label_3.setText(_translate("Form", "BPM"))
        self.adicionar_bpm.setText(_translate("Form", "A d i c i o n a r"))
        self.excluir_bpm.setText(_translate("Form", "E x c l u i r"))
        self.adicionar_banco_dados.setText(_translate("Form", "A d i c i o n a r"))