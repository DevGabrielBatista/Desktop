import mysql.connector
class plantamode1:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas_db"
        )
        self.cursor = self.conexao.cursor()

    def inserir_planta(self, nome_popular, nome_cientifico, imagem_path):
        sql = "INSERT INTO plantas (nome_popular, nome_cientifico, imagem_path) VALUES (%s, %s, %s)"
        valores = (nome_popular, nome_cientifico, imagem_path)
        self.cursor.execute(sql,valores)
        self.conexao.commit()
        return self.cursor.lastrowid
    
    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close() 