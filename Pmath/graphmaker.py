import matplotlib.pyplot as plt
import math
import numpy as np

def gm():
    #print("---------- Quadratic equation graph maker ---------- v.0.68")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    elif d == 0:
        x0 = (-b + d) / (2 * a)
    else:
        print("delta value is less than zero, there is no solution in R")
        exit()

    xv = -b / 2 * a
    yv = -d / 4 * a
    roots = [xv,yv]
    def parabola(x,a,b,c):
        y = a*x**2 + b*x + c
        return y
    # plot function
    x = np.linspace(int(xv)-5,int(yv)+5,100)
    y = parabola(x,a,b,c)
    plt.plot(x,y)
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    plt.text(xv-0.5, yv-3, '[' + str(round(xv,2)) +',' + str(round(yv,2)) + ']',color='orange', fontsize=9)
    plt.plot(xv, yv, marker="o")
    plt.plot(0, c, marker="o", color='yellow')
    if d > 0:
        plt.plot(x1, 0, marker="o", color='green')
        plt.text(x1 - 0.5, 2, '[' + str(round(x1,2)) + ']', color='green', fontsize=9)
        plt.plot(x2, 0, marker="o", color='green')
        plt.text(x2 - 0.5, 2, '[' + str(round(x2,2)) + ']', color='green', fontsize=9)

    if d == 0:
        plt.plot(x0, 0, marker="o", color='green')
        plt.text(x0 - 0.5, 2, '[' + str(round(x0,2)) + ']', color='green', fontsize=9)

    plt.show()

if __name__ == "__main__":
    gm()