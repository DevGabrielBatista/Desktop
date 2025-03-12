import mysql.connector

class Plantamode2:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas_db"
        )
        self.cursor = self.conexao.cursor()

    def inserir_dados(self, umidade, luminosidade, temperatura):
        sql = 'INSERT INTO dados (umidade, luminosidade, temperatura) VALUES (%s, %s, %s)'
        valores = (umidade, luminosidade, temperatura)
        self.cursor.execute(sql,valores)
        self.conexao.commit()
        return self.cursor.lastrowid
    
    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()