
# simple program do learn quadratic equations and find zeros of a function
def rf():
    print("---------- Quadratic equation root finder ---------- v.0.22")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # delta = 0 if a = 3 b = 24 and c = 48
    d = b * b - 4 * a * c


    if d > 0:
        print("delta(",d,") is greater than 0")
        x1 = (-b + d) / (2*a)
        x2 = (-b - d) / (2*a)
        print("x1 value is", x1, "and x2 value is",x2)

    elif d == 0:
        print("delta is",d)
        x = (-b + d) / (2*a)
        print("x1 value is equal to x2 value, so x is",x)

    else:
        print("the value of delta(",d,")is less than zero, there is no solution in R")

if __name__ == "__main__":
    rf()


