# Basquete de Robôs
# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/basquete/

entrada = int(input("Digite a distância do robô: "))

if entrada <= 2000:
    if entrada <= 800:
        print("A cesta vale 1 ponto")
    elif entrada <= 1400:
        print("A cesta vale 2 pontos")
    else:
        print("A cesta vale 3 pontos")
else:
    print("Distância fora do range")