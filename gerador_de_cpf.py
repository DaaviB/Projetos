"""
CPF = 168.995.350-09
=======================================
1 x 10 = 10						#				1 x 11 = 11
6 x 9 = 54						  #				6 x 10 =  60
8 x 8 = 64						  #				8 x 9 = 72
9 x 7 = 63						  #				9 x 8 = 72
9 x 6 = 54						  #				9 x 7 = 63
5 x 5 = 25  					    #				5 x 6 = 30
3 x 4 = 12					      #				3 x 5 = 15
5 x 3 = 15						  #				5 x 4 = 20
0 x 2 = 0							#				0 x 3 = 0
											#				0 x 2 = 0
		297												343
														11 x-(343 % 11) = 9
11 - (297 % 11) = 11						Digito 2 = 9
11 > 9 = 0
Digito 1 = 0
"""
# 9 primeiros digitos
from random import randint
numero = str(randint(100000000, 999999999))
cpf = numero
novo = cpf[:9]

digito_1 = 0
for x in range(0, 9):
	if novo[x].isnumeric():
		digito_1 += int(novo[x]) * (10 - x)
digito_1  = 11 - (digito_1 % 11)
if digito_1 > 9:
	digito_1 = 0
# ====================================== #

digito_2= 0
novo =str( novo) + str(digito_1)
for x in range(0, 10):
	if novo[x].isnumeric():
		digito_2 += int(novo[x]) * (11 - x)
digito_2 = 11 - (digito_2 % 11)
if digito_2 > 9:
	digito_2 = 0
novo = novo + str(digito_2)
print(novo)