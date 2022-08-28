import time

from Pmath import rootfinder, vertexfinder, graphmaker


def game_select():
    print("---------- Quadratic equation properties solver ---------- v.0.43")

    f = input("solve: (1) roots in R. (2) Vertex coordinates. (3) graph  ")

    if int(f) == 1:
        print("loading...")
        time.sleep(2)
        rootfinder.rf()
    elif int(f) == 2:
        print("loading...")
        time.sleep(2)
        vertexfinder.vf()
    elif int(f) == 3:
        print("loading...")
        time.sleep(2)
        graphmaker.gm()




if __name__ == "__main__":
    game_select()