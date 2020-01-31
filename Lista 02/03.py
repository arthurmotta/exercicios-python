#3.	Crie um algoritmo que leia dois números e mostre o maior número.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")