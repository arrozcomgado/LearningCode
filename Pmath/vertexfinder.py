# simple program to find vertex of an quadratic equation

def vf():
    print("---------- Quadratic equation vertex finder ---------- v.0.11")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = b * b - 4 * a * c

    xv = -b / 2*a
    yv = -d / 4*a
    print("the vertex is:(",xv,",",yv,")")

if __name__ == "__main__":
    vf()
