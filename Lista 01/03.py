# 3.	Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC. 
# IMC = peso / altura² 

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

print("O seu IMC é: " + str(imc))