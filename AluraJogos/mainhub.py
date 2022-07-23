import jogoadivinhacao
import forca
import time

def game_select():
    print("*********************************")
    print("****Bem vindo ao hub de jogos****")
    print("*********************************")


    print("(1) adivinhação (2) forca")
    jogo_escolha = int(input("Escolha um jogo:"))

    if jogo_escolha == 1:
        print("Loading adivinhação...")
        time.sleep(2)
        print("Done")
        time.sleep(1)
        print("")
        jogoadivinhacao.jogar()
    elif jogo_escolha == 2:
        print("Loading forca...")
        time.sleep(2)
        print("Done")
        time.sleep(1)
        forca.jogar()
if __name__ == "__main__":
    game_select()

