#9.	Crie um algoritmo que receba um número inteiro, 
# que representa um determinado mês do ano, 
# e mostre o nome do mês correspondente. 
# Por exemplo, se for informado o número 2, 
# algoritmo deverá exibir fevereiro. 
# O algoritmo deve validar se a entrada está correta.

meses = {
    "1": "Janeiro",
    "2": "Fevereiro",
    "3": "Março",
    "4": "Abril",
    "5": "Maio",
    "6": "Junho",
    "7": "Julho",
    "8": "Agosto",
    "9": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro",
}

numero = input("Digite um número para o mês: ")
if int(numero) > 12:
    print("Entrada inválida")
else:
    x = meses[numero]
    print(x)