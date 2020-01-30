# 5.	Um motorista deseja abastecer um valor X em reais, de combustível. 
# Escreva um algoritmo para ler o preço do litro do combustível e o valor que o motorista deseja abastecer. 
# Em seguida, informe quantos litros foram abastecidos.

combLitro = 3 #float(input("Digite o valor do litro combustivel: "))
valor = 12 #float(input("Digite o valor em reais a ser abastecido: "))

litros = (combLitro * valor) / valor

print(f"{litros}")