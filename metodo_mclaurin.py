#SERIE DE MCLAURIN
from math import *


def fat(n):
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            factorial = factorial * i
        #print("Fatorial de ",n , " is : ",factorial)
    return factorial


def func(a, b, c, d, x):
    f = (a + 2) * sin(x) + (c + d + 2)
    return f


def main(a, b, c, d, x):
    print(round(x, 10), sin(x))
    n = 3
    s = x
    f = "-"
    m=int(input("Digite o número de iterações: "))
    msg = "sen(x)-> x"
    for i in range(m):
        if (f == "+"):
            s = s + round((x ** n) / fat(n), 10)
            s = round(s, 10)
            f = "-"
        elif (f == "-"):
            s = s - round((x ** n) / fat(n), 10)
            s = round(s, 10)
            f = "+"
        n = n + 2
    print(sin(x))
    print(round(s))
    f = (a + 2) * s + (c + d + 2)
    return f


if __name__ == "__main__":
    a = int(input("A :"))
    b = int(input("B :"))
    c = int(input("C :"))
    d = int(input("D :"))

    x = (((b + 3) * pi) / 3)
    serie = main(a, b, c, d, x)
    print("Função :", round(func(a, b, c, d, x), 10), "---", "Função por McLaurin", round(serie, 10))
    print(abs(round(func(a, b, c, d, x), 10) - round(serie,10)))
