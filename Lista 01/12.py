#12.	Crie um algoritmo que calcule a área de uma esfera,
# sendo que o comprimento do raio é informado pelo usuário. 
# A área da esfera é calculada multiplicando-se 4 vezes pi e o raio ao quadrado.

raio = float(input("Informe o comprimento do raio: "))

area = (4 * 3.14) * raio ** 2

print("A área da esfera é: " + area)