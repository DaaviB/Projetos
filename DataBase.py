import os
import sqlite3
from  sqlite3 import Error

class DataBase:
    def __init__(self, nome, telefone, email):
        self.nome_c = "NOME_C"
        self.nome  = nome
        self.telefone = telefone
        self.email = email
        self.tabela()
        self.select()
        self.select()
    
    
    def conexao(self):
        print('Conectando ao Banco de Dados.')
        self.con = None
        try:
            self.con = sqlite3.connect("Base.db")
            self.cursor = self.con.cursor()
        except Error as ex:
            print(ex)
        return self.con
        
    
    def desconecta(self):
        print('Desconectando do Banco de Dados. ')
        self.con.close()
    
    
       
    def tabela(self):
        self.conexao()
        print("Criando Tabela. ")
        try:
       	 self.cursor.execute("""CREATE TABLE IF NOT EXISTS dados_db (
        												ID_C INTEGER PRIMARY KEY AUTOINCREMENT,
        												NOME_C  VARCHAR(30) NOT NULL,
        												TELEFONE_C VARCHAR(14),
        												EMAIL_C VARCHAR(30) NOT NULL
        												)
        										""")
        except Error as ex:
        	print(ex)
        self.con.commit()
        self.desconecta()
    
    
    def inserir(self):
    	self.conexao()
    	try:
    		self.cursor.execute("""INSERT INTO dados_db (NOME_C, 
    													TELEFONE_C, 
    													EMAIL_C) 
    													VALUES(?, ?, ? )""", (self.nome, self.telefone, self.email))
    	except Error as ex:
    		print(ex)
    	self.con.commit()
    	print("Dados Inserido. ")
    	self.desconecta()
    
    
    def delete(self):
    	self.conexao()
    	try:
    		self.cursor.execute("DELETE FROM dados_db")
    		self.con.commit()
    		print("Dados deletados. ")
    	except Error as ex:
    		print(ex)
    	self.desconecta()
    
    
    def update(self):
    		self.conexao()
    		try:
    			self.cursor.execute("UPDATE dados_db SET %s = '' WHERE ID_C=25"%(self.nome_c,))
    			self.con.commit()
    			print("Dados Atualizados com sucesso. ")
    		except Error as ex:
    			print(ex)
    		self.desconecta()
    
    
    def select(self):
    		self.conexao()
    		print('Consultando os Dados da Tabela. ')
    		self.cursor.execute("SELECT * FROM dados_db")
    		dados = self.cursor.fetchall()
    		for p in dados:
    			print(p)
    			
    		
Nome = str(input("Nome: "))
Telefone = int(input("Telefone: "))
Email = str(input("Email: "))
Banco = DataBase(Nome, Telefone, Email)