#2.	Recrie o algoritmo de cálculo de média das notas, mas, desta vez, 
# calcule a média ponderada, sabendo que a primeira nota possui peso 1, 
# a segunda nota possui peso 2 e a terceira nota possui peso 3.

n1 = int(input("Entre com a primeira nota: "))
n2 = int(input("Entre com a segunda nota: "))
n3 = int(input("Entre com a terceira nota: "))

final = ((n1 * 1) + (n2 * 2) + (n3 * 3)) / 6

print("A média ponderada é do aluno é: " + str(final))