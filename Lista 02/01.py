#1.	Crie um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.

numero = int(input("Digite um número: "))

if numero < 0:
    print("O número é negativo!")
elif numero == 0:
    print("O número é igual a 0!")
else:
    print("O número é positivo!")