
#Exercício 1
def verifica_numeros(numero):
    if numero > 0:
        print("O numero é positivo")
    elif numero < 0:
        print("O numero é negativo")
    else:
        print("Este numero é o zero")
numero = float(input("Digite um numero:"))
verifica_numeros(numero)

#Exercício 2

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

if num1 > num2:
    print(f"O {num1} é maior que o {num2}")
elif num2 > num1:
    print(f"O {num2} é maior que o {num1}")
else:
    print("Esses numeros sao iguais")

#Exercícios 3

numero = float(input("Digite um numero:"))

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")

#Exercício 4

ano = float(input("Digite um ano:"))

if ano % 4 == 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")

#Exercício 5
def maior(num1, num2, num3):
    maior = max(num1, num2, num3)
    print(f"O maior numero é o {maior}")

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
num3 = float(input("Digite o terceiro numero:"))
maior(num1, num2, num3)

#Exercício 6

idade = float(input("Digite sua idade:"))

if idade > 18:
    print("Voce pode votar!")
else:
    print("Voce não pode votar")

#Exercício 7


#Exercício 8

def Digite_Senha(senha):
    if senha == 1234:
        print("SENHA CORRETA")
    else:
        print("SENHA INCORRETA")

senha = float(input("Digite a senha:"))
Digite_Senha(senha)

#Exercício 9

def Entre_Numeros(num):
    if 10 <= num <= 50:
        print("O numero está entre 10 e 50")
    else:
        print("O numero não esta entre 10 e 50")

num = float(input("Digite um numero:"))
Entre_Numeros(num)

#Exercício 10

def Alto_Baixo(num):
    if num > 100:
        print("Alto")
    else:
        print("Baixo")

num = float(input("Digite um numero:"))
Alto_Baixo(num)



def Maior_numero(num1, num2): 
    if num1 > num2:
        print(f"O {num1} é maior que o {num2}")
    elif num2 > num1:
        print(f"O {num2} é maior que o {num1}")
    else:
        print("Esses numeros sao iguais")

n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))
Maior_numero(n1, n2)