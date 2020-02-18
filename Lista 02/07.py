#1.	Crie um algoritmo que calcule e mostre o novo valor de um salário 
# a partir das seguintes regras: salários de até R$ 1.000,00 
# inclusive recebem 30% de aumento, salários de até R$ 2.000,00 
# inclusive recebem 25%, salários de até R$ 3.000,00 
# inclusive recebem 20%, salários de até R$ 4.000,00 
# inclusive recebem 15% e 
# salários acima de R$ 4.000,00 recebem apenas 10%.

salario = float(input("Digite seu salário: "))

if salario <= 1000:
    reajuste = (salario / 100) * 30
    print(f"O salário com reajuste de 30% fica em R${reajuste+salario}")
elif salario <= 2000:
    reajuste = (salario / 100) * 25
    print(f"O salário com reajuste de 25% fica em R${reajuste+salario}")
elif salario <= 3000:
    reajuste = (salario / 100) * 20
    print(f"O salário com reajuste de 20% fica em R${reajuste+salario}")
elif salario <= 4000:
    reajuste = (salario / 100) * 15
    print(f"O salário com reajuste de 15% fica em R${reajuste+salario}")
else:
    reajuste = (salario / 100) * 10
    print(f"O salário com reajuste de 10% fica em R${reajuste+salario}")

    
        