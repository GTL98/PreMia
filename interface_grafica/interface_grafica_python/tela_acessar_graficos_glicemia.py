# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_acessar_graficos_glicemia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 400)
        Form.setMinimumSize(QtCore.QSize(350, 400))
        Form.setMaximumSize(QtCore.QSize(350, 400))
        Form.setStyleSheet("QPushButton#abrir{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px\n"
"}\n"
"QPushButton#abrir:hover{\n"
"background-color: rgba(145, 207, 230, 200)\n"
"}\n"
"QPushButton#abrir:pressed{\n"
"background-color: rgba(150, 150, 150, 255);\n"
"padding-top: 2px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
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
        self.horizontalLayout.addWidget(self.ajuda)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(11, 27, 271, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.media = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.media.setFont(font)
        self.media.setObjectName("media")
        self.verticalLayout.addWidget(self.media)
        self.desvio_padrao = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.desvio_padrao.setFont(font)
        self.desvio_padrao.setObjectName("desvio_padrao")
        self.verticalLayout.addWidget(self.desvio_padrao)
        self.variabilidade = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.variabilidade.setFont(font)
        self.variabilidade.setObjectName("variabilidade")
        self.verticalLayout.addWidget(self.variabilidade)
        self.massa = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.massa.setFont(font)
        self.massa.setObjectName("massa")
        self.verticalLayout.addWidget(self.massa)
        self.colher = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.colher.setFont(font)
        self.colher.setObjectName("colher")
        self.verticalLayout.addWidget(self.colher)
        self.margem = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.margem.setFont(font)
        self.margem.setObjectName("margem")
        self.verticalLayout.addWidget(self.margem)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.abrir = QtWidgets.QPushButton(Form)
        self.abrir.setMinimumSize(QtCore.QSize(120, 40))
        self.abrir.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.abrir.setFont(font)
        self.abrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.abrir.setObjectName("abrir")
        self.verticalLayout_2.addWidget(self.abrir, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Gráficos Glicemia"))
        self.ajuda.setText(_translate("Form", "?"))
        self.groupBox.setTitle(_translate("Form", "Gráficos Glicemia"))
        self.media.setText(_translate("Form", "Média"))
        self.desvio_padrao.setText(_translate("Form", "Desvio Padrão"))
        self.variabilidade.setText(_translate("Form", "Variabilidade"))
        self.massa.setText(_translate("Form", "Massa Glicose"))
        self.colher.setText(_translate("Form", "Colher de Chá"))
        self.margem.setText(_translate("Form", "Margem Glicêmica"))
        self.abrir.setText(_translate("Form", "A b r i r"))
