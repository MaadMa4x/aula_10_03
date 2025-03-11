print("SEJA MUITO BEM VINDO AO JOGO DE ADIVINHAÇÃO")
import random

numero_secreto=random.randint(1,10)
tentativas=0
max_tentativas=3

print("tente adivinhar o número entre 1 e 10")
while tentativas < max_tentativas:
    palpite=int(input("digite eu palpite:"))
    tentativas += 1 
    if palpite==numero_secreto:
        print("Parabéns, você acertou!")
    elif palpite < numero_secreto:
        print("Muito baixo, tente novamente")
    else:
        print("Muito alto, tente novamente")

palpite != numero_secreto
print ("Fim do jogo.O número era: " ,numero_secreto)


    