#Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. 
#Os endereços no intervalo de 0 a 127 são classe A, 
#de 128 a 191 são classe B, 
#de 192 a 223 são classe C, 
#de 224 a 239 são classe D 
#e a partir de 240 são classe E. 
#Crie um algoritmo que leia o primeiro octeto, 
#no formato decimal, de um endereço IP e informe a sua classe.

ip = input("Digite o endereço de IP: ")
octeto = int(ip[:3])

if octeto <= 127:
    print("Esse IPV4 é classe A.")
elif octeto <= 191:
    print("Esse IPV4 é classe B.")
elif octeto <= 223:
    print("Esse IPV4 é classe C.")
elif octeto <= 239:
    print("Esse IPV4 é classe D.")
else:
    print("Esse IPV4 é classe E.")
