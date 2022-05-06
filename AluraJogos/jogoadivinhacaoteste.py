

#NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING NOT WORKING


import random
import time
from termcolor import colored


print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")



numero_secreto = 42 #random.randint(1, 101)
tentativas = 5
rodadas = 1
play = True

while play:
    start = time.time()
    while (rodadas <= tentativas) and True:
        print("Total de tentativas: {} de {}".format(rodadas, tentativas))
        chute = input("Digite um número: ",)
        try:
            chute_int = int(chute)
            print("Você digitou: ", chute_int,)
            acertou = chute_int == numero_secreto
            menor = chute_int > numero_secreto
            maior = chute_int < numero_secreto
            if not acertou:
                if (menor):
                    print("Você errou, o número secreto é menor que", chute_int)
                elif (maior):
                    print("Você errou, o número secreto é maior que", chute_int)
                    rodadas += 1
            else:
                print(colored("Você acertou o número secreto, parabéns!", 'green'))
                tentativas = -1
                end = time.time()
                tempo = end - start
                print("Tempo:",round(tempo, 2))

        except ValueError:
            try:
                float(chute)
                print("O número colocado não é valido")
            except ValueError:
                print("Não foi detectado um número. Por favor escreva um número válido")



if tentativas == 5:
    print(colored("Você perdeu!", "red"))
    end = time.time()
    print("O número secreto era:", numero_secreto)
    tempo = end - start
    print("Tempo:",round(tempo, 2))


