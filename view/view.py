import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller_dd import PlantaController

class DadosPlanta(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = PlantaController()
        self.initUI()

    def botao_clicado(self):
        umidade = self.input_umidade.text().strip()
        temperatura = self.input_temperatura.text().strip()
        luminosidade = self.input_luminosidade.text().strip()

        if not umidade or not temperatura or not luminosidade:
            QMessageBox.critical(self, 'erro', 'preencha todos os campos!')
            return
        
        dados_id = self.controller.salvar_dados(umidade,luminosidade,temperatura)

        if dados_id:
            QMessageBox.information(self, 'sucesso', 'dados cadastrados!')

            self.input_umidade.clear()
            self.input_temperatura.clear()
            self.input_luminosidade.clear()

        else:
            QMessageBox.critical(self, 'erro', 'erro em slavar os dados.')

    
    def initUI(self):
        self.setWindowTitle("dados de plantas")
        self.setGeometry(200,100,200,100)
        self.setStyleSheet("background-color: green;")

        lele = QVBoxLayout()

        titulo = QLabel('Envie os dados')
        titulo.setFont(QFont("arial", 16, QFont.Bold))
        titulo.setStyleSheet('color: black;')

        self.input_umidade = QLineEdit()
        self.input_umidade.setPlaceholderText("insira umidade")
        self.input_umidade.setStyleSheet("background-color: yellow")
        self.input_umidade.move(1150,400)
        self.input_temperatura = QLineEdit()
        self.input_temperatura.setPlaceholderText('Insira temperatura')
        self.input_temperatura.move(600,400)
        self.input_temperatura.setStyleSheet("background-color: yellow")
        self.input_luminosidade= QLineEdit()
        self.input_luminosidade.setPlaceholderText('Insira luminosidade')
        self.input_luminosidade.move(600,400)
        self.input_luminosidade.setStyleSheet("background-color: yellow")
        botao_canc = QPushButton('cancelar')
        botao_canc.move(600,600)
        botao_canc.setStyleSheet("background-color: red")
        botao_cad = QPushButton('cadastrar')
        botao_cad.move(1300,600)
        botao_cad.setStyleSheet('background-color: green')
        botao_cad.clicked.connect(self.botao_clicado)

        lele.addWidget(self.input_umidade)
        lele.addWidget(self.input_luminosidade)
        lele.addWidget(self.input_temperatura)
        lele.addWidget(titulo)
        lele.addWidget(botao_canc)
        lele.addWidget(botao_cad)

        self.setLayout(lele)