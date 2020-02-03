#5.	Crie um algoritmo que leia três números e mostre-os em ordem crescente.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = 0
menor = 0
meio  = 0

if n1 >= n2 and n1 >= n3:                   #Faz as duas primeiras comparações (!!!!!!Quebrando as comparações por partes!!!!!)
  maior = n1                                #Salva o valor maior em uma variável 
  if n2 >= n3:                              #Faz as outras comparações
    meio = n2
    menor = n3
  else:
    meio = n3
    menor = n2

elif n2 >= n3:
  maior = n2
  if n1 >= n3:
    meio = n1
    menor = n3
  else:
    meio = n3
    menor = n1

else:
  maior = n3
  if n1 >= n2:
    meio = n1
    menor = n2
  else:
    meio = n2
    menor = n1 

print(f"A ordem é: {menor}, {meio} e {maior}.")
