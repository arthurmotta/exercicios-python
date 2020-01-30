# 1.	Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno e, em seguida, informe a média entre elas.

n1 = int(input("Entre com a nota: "))
n2 = int(input("Entre com a nota: "))
n3 = int(input("Entre com a nota: "))

final = (n1 + n2 + n3) / 3

print("A média é do aluno é: " + str(final))