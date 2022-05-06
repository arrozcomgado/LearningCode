from termcolor import colored

n = 0
while n > -1:
    try:
        lst = []
        n = int(input("Escreva a quantidade de elementos a ser definido a média:"))
        print("Escreva os elementos desejados")


        for i in range(0, n):
            ele = int(input())
            lst.append(ele)

        media = sum(lst)/len(lst)
        formatted_media = "{:.2f}".format(media)
        print("A média é:", float(formatted_media))
        n = n*0 - 1


    except ValueError:
        try:
            str(lst)
            print(colored("Por favor coloque um número válido",'red'))
        except ValueError:
            print(colored("O número colocado não é aceito",'red'))



