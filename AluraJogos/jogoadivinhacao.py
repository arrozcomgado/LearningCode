import random
import time
from termcolor import colored


print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


#Variaveis
numero_secreto = random.randint(1, 101)
tentativas = 5
rodadas = 1

#cronometro start
start = time.time()
#check user input(float,int, string)
while (rodadas <= tentativas) and True:

    print(colored("Total de tentativas: {} de {}".format(rodadas, tentativas), "cyan"))
    chute = input("Digite um número: ",)
    try:
        chute_int = int(chute)
        if chute_int < 1 or chute_int > 100:
            print(colored("Coloque um número entre 1 e 100, o número colocado não é aceito", "red"))
            continue
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
            break
    except ValueError:
        try:
            float(chute)
            print(colored("O número colocado não é valido","red"))

        except ValueError:
            print(colored("Não foi detectado um número. Por favor escreva um número válido","red"))




if tentativas == 5:
    print(colored("Você perdeu!", "red"))
    end = time.time()
    print("O número secreto era:", numero_secreto)
    tempo = end - start
    print("Tempo:",round(tempo, 2))

