#13.	Crie um algoritmo que calcule o volume de uma caixa d’água cilíndrica, 
# sendo que os comprimentos do raio e a altura são informados pelo usuário. 
# O volume é calculado multiplicando-se pi, o raio ao quadrado e a altura.

raio = float(input("Informe o raio: "))
altura = float(input("Informe a altura: "))

volume = round(3.14 * raio ** 2 * altura, 2)

print(f"O volume da caixa d'água é de: {volume}")