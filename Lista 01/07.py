# 7.	Crie um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante.
# A gorjeta é calculada como sendo 10% do valor da conta, que deve ser informado pelo usuário.

valor = float(input("Digite o valor da conta: "))

final = (valor * 10) / 100

print(f"O valor da gorjeta será de: {final}")