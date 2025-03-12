import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller_cp import plantacontroller

class cadastroplantas(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = plantacontroller()
        self.imagem_path= ""
        self.tela_princ()

    def botao_clicado(self):
        nome_popular = self.input_nome_popular.text().strip()
        nome_cientifico = self.input_nome_cientifico.text().strip()

        if not nome_popular or not nome_cientifico:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")  
            return 
        
        planta_id = self.controller.salvar_plantas(nome_popular, nome_cientifico, self.imagem_path)

        if planta_id:
            QMessageBox.information(self, "Sucesso", "Planta cadastrada com sucesso!")  # Exibe mensagem de sucesso
            
            self.input_nome_popular.clear()
            self.input_nome_cientifico.clear()
            self.botao_imagem.clear()
            self.imagem_path = "" 
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar a planta.")

    
    def tela_princ(self):
        self.setWindowTitle("cadastro de plantas")
        self.setGeometry(200,100,200,100)
        self.setStyleSheet("background-color: green;")

        laylay = QVBoxLayout()

        titulo = QLabel("Faça o cadastro!")
        titulo.setFont(QFont("Arial", 16, QFont.Bold))
        titulo.setStyleSheet("color: black;")

        self.input_nome_popular = QLineEdit()
        self.input_nome_popular.setPlaceholderText("insira o nome popular")
        self.input_nome_popular.setStyleSheet("background-color: yellow")
        self.input_nome_popular.move(1150,400)
        self.input_nome_cientifico = QLineEdit()
        self.input_nome_cientifico.setPlaceholderText('nome cientifico')
        self.input_nome_cientifico.move(600,400)
        self.input_nome_cientifico.setStyleSheet("background-color: yellow")
        self.botao_imagem = QPushButton('insira uma imagem')
        self.botao_imagem.setStyleSheet("background-color: green;")
        self.botao_imagem.move(800,400)
        self.area_imagem = QLabel()
        self.area_imagem.setAlignment(Qt.AlignCenter)
        self.area_imagem.setStyleSheet("border: 1px solid black; min-height: 100px; background-color: green;")
        botao_canc = QPushButton('cancelar')
        botao_canc.move(600,600)
        botao_canc.setStyleSheet("background-color: red")
        botao_cad = QPushButton('cadastrar')
        botao_cad.move(1300,600)
        botao_cad.setStyleSheet('background-color: green')
        botao_cad.clicked.connect(self.botao_clicado)

        laylay.addWidget(titulo)
        laylay.addWidget(self.input_nome_popular)
        laylay.addWidget(self.input_nome_cientifico)
        laylay.addWidget(self.botao_imagem)
        laylay.addWidget(self.area_imagem)
        laylay.addWidget(botao_canc)
        laylay.addWidget(botao_cad)

        self.setLayout(laylay)

    def abrir_arquivo(self):
        options = QFileDialog.Options()  
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Abrir Arquivo", "", "Imagens (*.png *.jpg *.jpeg *.bmp *.gif);;Todos os Arquivos (*)", options=options
        )
        if file_name:  
            self.imagem_path = file_name  
            pixmap = QPixmap(file_name)  
            self.area_imagem.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio)) 








       

          
