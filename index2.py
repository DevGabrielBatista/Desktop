import sys
sys.path.append('c:/Users/gabriel.bsilva104/OneDrive - SENAC - SP/IhOrTS/atividade_umidade')

from PyQt5.QtWidgets import QApplication, QWidget
 


from view.tela import cadastroplantas

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = cadastroplantas() 
    janela.show()
    sys.exit(app.exec_()) 