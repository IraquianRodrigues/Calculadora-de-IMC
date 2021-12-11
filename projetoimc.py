#PROJETO IMC
#Autor: Iraquian Rodrigues

print('*'*20)

print('Calculando o IMC ')

print('*'*20)
print()

print('DADOS CADASTRAIS!')
print()

nome = input("Qua seu nome?: ")
idade = input("Informe sua idade: ")
peso = float(input("Quantos Kg pesa?: "))
altura = float(input("Sua altura?: "))

imc = float(peso / altura) ** 2

print()



import time
import sys
print("Calculando os Dados, Aguarde...")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.6)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

print(F'Seu nome é {nome}, tem {idade} anos e {altura} de altura.')
print(F'Seu resultado do seu IMC foi de {imc:.2f}')
print('De acordo com o cálculo voce está com o seguinte IMC:')

if imc < 0.17:
    print('abaixo do peso')

elif imc > 0.19 and imc <= 0.25:
    print('Está no peso ideal')

elif imc > 0.25 and imc <= 0.29:
    print('Levemente Acima do peso')

elif imc > 0.30 and imc <= 0.35:
    print('Obesidade de Grau I')

elif imc > 0.35 and imc <= 0.39:
    print('Obesidade de Grau II')

elif imc > 0.40:
    print('Obesidade Morbida')

else:
    print('Encerrar Programa!')
