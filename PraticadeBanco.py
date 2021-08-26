from Banco import *
from datetime import datetime
from time import sleep

# >>> PASSAGEM DE DADOS PARA O BANCO <<< #
class Dados(Base):
		
		
	def __init__(self):
		self.id = 0
		self.table()
		self.menu_principal()
		

# >>> CHAMADA DAS FUNÇÕES DO BANCO <<< #
	def passagem(self, answer=0):
		if answer == 1:
			self.insert()
			print("\x1b[2J\x1b[1;1H", end='')
			self.select(idc=True)
		elif answer == 2:
			print("\x1b[2J\x1b[1;1H", end='')
			self.select()
		elif answer == 3:
			print("\x1b[2J\x1b[1;1H", end='')
			self.update()
		elif answer == 4:
			print("\x1b[2J\x1b[1;1H", end='')
			self.delete()
		

# >>> MENU PRINCIPAL <<< #		
	def menu_principal(self):
		while True:
			print("\x1b[2J\x1b[1;1H")
			print(f"{'= = = = REGISTRATION FIELD = = = = '}\n".center(70))
			print(f"{'Bem vindo!!Escolha uma das Opções.'}\n".center(70))
			print(f"{'[ 1 ]: New register'}")
			print(f"{'[ 2 ]: Select register'}")
			print(f"{'[ 3 ]: Update register'}")
			print(f"{'[ 4 ]: Delete register'}")
			print(f"{'[ 5 ]: Limpar tela.'}")
			print(f"\n{'[ 0 ]: Quit'}\n")
			while True:
				try:
					answer = int(input("[ ? ] Opcão: "))
					if answer:
						# CHAMADA/NEW_REGISTER
						if answer== 1:
							print("\x1b[2J\x1b[1;1H", end='')
							self.new_register()
						# CHAMADA/SELECT_REGISTER
						elif answer  == 2:
							print("\x1b[2J\x1b[1;1H", end='')
							self.select_register()
						# CHAMADA/UPDATE_REGISTER
						elif  answer == 3:
							print("\x1b[2J\x1b[1;1H", end='')
							self.update_register()
						# CHAMADA/DELETE_REGISTER
						elif answer == 4:
							print("\x1b[2J\x1b[1;1H", end='')
							self.delete_register()
						elif answer == 5:
						# LIMPAR_TELA
							print("\x1b[2J\x1b[1;1H", end='')
							self.menu_principal()
						else:
							print("Opção inexistente.")
					else:
						exit()
				except Exception as ex:
					print('Opção inválida.')


# >>> NEW REGISTER <<< #
	def  new_register(self):
		print('='*72)
		print(" > > > NEW REGISTER < < < ".center(72))
		print('='*72)
		self.hour_register = datetime.now().strftime("%y-%m-%d[%H:%M]")
		while True:
				try:
					self.name = str(input('Nome: ')).strip()
					if self.name:
						break
					else:
						print("Campo em branco. ")
				except:
					print('Ocorreu um erro.')
		while True:
				try:
					self.gender = str(input("Sexo [ F / M ]: ")).upper().strip()[0:3]
					if self.gender:
						if self.gender in "FEMA":
							break
						else:
							raise Exception
					else:
						print("Campo em branco.")
				except:
					print("Ocorreu um erro. ")
		while True:
				try:
					self.telephone = int(input('Telepone: '))
					break
				except:
					print("Ocorreu um erro.")
		while True:
				try:
					self.city = str(input('Cidade: ')).capitalize().strip()
					if not self.city:
						print("Campo em branco. ")
					else:
						break
				except:
					print("Ocorreu um erro. ")
		# > PASSAGEM < #
		self.passagem(1)
		print("> [ >>> Novo registro inserido com sucesso <<< ] <".center(70))
		while True:
			print()
			flag = str(input("[ >>> Press <ENTER> para voltar ao Menu <<< ]".center(70)))
			if not flag:
				self.menu_principal()
			else:
				continue


# >>> SELECT REGISTER <<< #
	def select_register(self):
		print('='*72)
		print("> > > SELECT REGISTER < < <".center(72))
		print('='*72)
		while True:
			print("[ > > > Press <ENTER>, ou digite um ID < < < ]".center(72))
			try:
				self.id = str(input("[ ID ]: ")).strip()
				if self.id:
					if self.id.isnumeric():
						print("\x1b[2J\x1b[1;1H", end='')
						# > PASSAGEM < #
						self.passagem(answer=2)
					else:
						print("\x1b[2J\x1b[1;1H", end='')
						continue
				else:
					# > PASSAGEM < #
					self.passagem(answer=2)
			except Exception as ex:
				print("Ocorreu um erro.")
				print(ex)
			print()
			while True:
				flag = str(input("[ >>> Press <ENTER> para voltar ao Menu: <<< ]".center(70))).strip()
				if not flag:
					self.menu_principal()
				else:
					continue


# >>> UPDATE REGISTER <<< #
	def update_register(self):
		print('='*72)
		print("> > > UPDATE REGISTER < < <".center(72))
		print('='*72)
		try:
			while True:
				print( '[ > > > Digite o ID do registro < < < ]'.center(70))
				self.id = str(input("[ ID ]: ")).strip()
				print('='*70)
				if not self.id:
					print("\x1b[2J\x1b[1;1H", end='')
					continue
				else:
					if self.id.isalpha():
						print("\x1b[2J\x1b[1;1H", end='')
						continue
					elif not self.id.isnumeric():
						print("\x1b[2J\x1b[1;1H", end='')
						continue
				print('[ >>> Escolha o Campo que deseja modificar: <<< ]'.center(70))
				print('-'*72)
				print("|[ 1 ]: Nome | "
							"[ 2 ]: Sexo | "
							"[ 3 ]: Telefone | "
							"[ 4 ]: Cidade |"
							.center(72)
							)
				print('-'*72)
				print('='*70)
				self.select()
				# >>> ENTRADA <<< #
				while True:
					self.escolha = str(input('Campo [ ? ]:')).strip()
					# >>> TRATAMENTO <<< # 
					if self.escolha:
						if self.escolha.isnumeric():
							self.escolha =int(self.escolha)
							# 1° NOVO NOME # 
							if self.escolha == 1:
								self.column = "NAME"
								while True:
									self.campo = str(input("Nome: ")).strip().title()
									if not self.campo:
										print("Campo em branco!")
										continue
									else:
										break
							# 2° NOVO SEXO #
							elif self.escolha == 2:
								self.column = "GENDER"
								while True:
									self.campo = str(input("Sexo [ F / M ]: ")).strip().upper()[0:3]
									if self.campo:
										if self.campo in "FEMMAS":
											break
										else:
											print("Digite F ou M.")
									else:
										print("Campo em branco!")
							# 3° NOVO TELEFONE # 
							elif self.escolha == 3:
								self.column = "TELEPHONE"
								while True:
									try:
										self.campo = int(input("Telefone: "))
										break
									except Exception:
										print("Digite um número válido!")
							# 4° NOVA CIDADE #
							elif self.escolha == 4:
								self.column = "CITY"
								while True:
									self.campo = str(input("Cidade: ")).title().strip()
									if self.campo:
										for letra in self.campo:
											pass
										if letra.isnumeric():
											print("O campo cidade "
											"não deve conter números!"
											)
											continue
										elif not letra.isalpha():
											print("O campo cidade "
											"não deve conter caracteres especias!"
											)
											continue
										else:
											break
									else:
										print("Campo em branco!")
										continue
					# >>> TRATAMENTO <<< #	
							else:
								print("Opção não existe! ")
								continue
						else:
							print("Opção inválida!")
							continue
					else:
						print("Campo em branco!")
						continue
					#  > PASSAGEM < #
					self.passagem(answer=3)
					while True:
						print()
						flag = str(input("[ >>> Press <ENTER> para voltar ao Menu <<< ]".center(70)))
						if not flag:
							self.menu_principal()
						else:
							continue
		except Exception as ex:
			print("Ocorreu um erro! Tente novamente. ")
			exit()


# >>> DELETE REGISTER <<< #
	def delete_register(self):
		while True:
			try:
				print("[ >>> Digite o ID que deseja DELETAR <<< ]".center(70))
				self.id = str(input("[ ID ]: ")).strip()
				if self.id:
					if self.id.isnumeric():
						# > PASSAGEM < #
						self.passagem(4)
					else:
						print("Valor inválido!")
						sleep(0.3)
						print("\x1b[2J\x1b[1;1H", end='')
						continue
				else:
					print("Campo em branco!")
					sleep(0.3)
					print("\x1b[2J\x1b[1;1H", end='')
					continue
			except:
				print("Ocorreu um erro! Tente novamente.")
			while True:
						print()
						flag = str(input("[ >>> Press <ENTER> para voltar ao Menu <<< ]".center(70)))
						if not flag:
							self.menu_principal()
						else:
							continue


cadastro_dados = Dados()