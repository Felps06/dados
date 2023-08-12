# nome, sobrenome, idade, altura, peso, maior_de_idade #

nome = "Felipe"

sobrenome = "Gabriel"

idade = 17

altura = 1.84

peso = 105

maior_de_idade = idade >= 18

print("nome", nome)
print("sobrenome", sobrenome)
print("idade", idade, "anos")
print("altura", altura, "metros")
print("peso", peso, "kg")
print("maior_de_idade", "sim" if maior_de_idade else "não")


sair = "sair"

numero01 = input("digite o primeiro numero")
numero02 = input("digite o segundo numero")
operador = input("digite o operador (+-*/)")
 

numero01_float = 0
numero02_float = 0

numero01_float = float(numero01)
numero02_float = float(numero02)

if operador == "+":
 print(f"{numero01_float} + {numero02_float} = " , numero02_float + numero01_float)

elif operador == "-":
 print(f"{numero01_float} - {numero02_float} = " , numero02_float - numero01_float)

elif operador == "*":
 print(f"{numero01_float} * {numero02_float} = " , numero02_float * numero01_float)

elif operador == "/":
 print(f"{numero01_float} / {numero02_float} = " , numero02_float / numero01_float)

