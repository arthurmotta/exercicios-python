#6.	Crie um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.

letra = input("Digite uma letra: ")

vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")