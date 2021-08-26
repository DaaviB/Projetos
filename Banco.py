import sqlite3 
from sqlite3 import Error



class Base:
	def connect(self):
		try:
			self.connection= sqlite3.connect("Base_REGISTER.db")
			self.cursor  = self.connection.cursor()
		except Error as ex:
			print(ex)

	
	def disconnect(self):
		self.connection.close()
			

	def table(self):
		self.connect()
		try:
			self.cursor.execute("""CREATE TABLE IF NOT EXISTS register_db (
														ID INTEGER PRIMARY KEY AUTOINCREMENT,
														NAME CHAR(20) NOT NULL,
														GENDER CHAR(10),
														TELEPHONE INTEGER(12),
														CITY CHAR(10),
														HOUR_REGISTER FLOATING(20))
													""")
			self.connection.commit()
			print('Table created sucessfully. ')
			self.disconnect()
		except Error as ex:
			print(ex)
	
	
	def insert(self):
		try:
			self.connect()
			self.cursor.execute("""INSERT INTO register_db (
														NAME,
														GENDER,
														TELEPHONE,
														CITY,
														HOUR_REGISTER)
														VALUES(?, ?, ?, ?, ?)""", ((
														self.name, 
														self.gender, 
														self.telephone, 
														self.city, 
														self.hour_register
														)))
			self.connection.commit()
			self.disconnect()
		except Error as ex:
			print(ex)
	
	
	def delete(self):
		try:
			self.connect()
			self.cursor.execute("DELETE FROM register_db WHERE ID= ?",((self.id)))
			self.connection.commit()
			self.disconnect()
		except Error as ex:
			print(ex)
	
	
	def update(self):
		self.connect()
		self.cursor.execute("UPDATE register_db SET %s=%s WHERE ID=?",((self.column, self.campo, self.id)))
		self.connection.commit()
		self.disconnect()
	
	def select(self, idc=False):
		self.connect()
		self.idc = idc
		if self.idc:
			self.cursor.execute("SELECT * FROM register_db ORDER by ID ASC")
			self.datas = self.cursor.fetchall()
			self.id = self.datas[-1][0]	
		if self.id:
			self.cursor.execute("SELECT * FROM register_db WHERE ID=:id ORDER by ID ASC", ((self.id, )))
		else:
			self.cursor.execute("SELECT * FROM register_db ORDER by ID ASC")
		self.datas = self.cursor.fetchall()
		try:
			if not self.id in self.datas[:][0]:
				pass
			print('='*72)
			print(f"|{'ID':^5}|{'NAME':^12}|{'GENDER':^8}|{'TELEPHONE':^12}|{'CITY':^13}|{'DATE/HOUR':^15}|")
			print('='*72)
			for field  in self.datas:
					print(f"|{field[0]:^5}|{field[1]:<12}|{field[2]:^8}|{field[3]:<12}|{field[4]:<13}|{field[5]:^10}|")
			print('='*72)
		except:
			print('='*72)
			print("[ >>> ID NÃO ENCONTRADO! Tente novamente. <<< ]".center(70))
			print('='*72)
		self.disconnect()

var = Base()