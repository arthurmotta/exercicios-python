#Crie um algoritmo que valide uma data, 
# formada por dia, mês e ano. Por exemplo, 
# a data 30/02 é sempre inválida; mas a data 29/02/2012 é válida.

data = input("Digite uma data: ")

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

if dia > 29 and mes == 2:
    print("Essa data é inválida!")
elif dia < 31 and mes < 12 and ano < 2099:
    print("Essa data é válida!")
else:
    print("Essa data é inválida!")


