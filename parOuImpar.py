import random
escolha = input("Qual você escolhe: (1) Par? ou (2) Ímpar?")
seuNumero = int(input("Digite um número de 0 a 10:"))
meuNumero = random.randint(0,10)
print ("Eu escolhi ", meuNumero)
somaNumeros = seuNumero + meuNumero
print("A soma do meu número e do seu deu: ", somaNumeros)
deuPar = (somaNumeros % 2 == 0)
if escolha == '1' and deuPar:
    print ("Você ganhou!")
elif escolha == '2' and not deuPar:
    print ("Você ganhou!")
else:
    print("Você perdeu!")

