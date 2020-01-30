#  8.	Crie um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste.
#  O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%.

salario = float(input("Valor do salário atual: "))
percentual = float(input("Percentual de reajuste: "))

reajuste = (salario * percentual) / 100

print(f"O salário com o reajuste fica em: {salario + reajuste}")