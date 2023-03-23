import cmath
from math import sqrt
from sys import float_info

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < float_info.epsilon: #sys.float_info.epsilon é o menor float positivo representável tal que 1,0 + epsilon != 1,0 na aritmética de ponto flutuante da máquina
                print("Zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

def solve_quadratic(a, b, c):
    d = b*b - 4*a*c #Discriminante
    if d < 0:
        root = cmath.sqrt(d)
    else:
        root = sqrt(d)
    x1 = (-b + root) / (2*a)
    x2 = (-b - root) / (2*a)
    return x1, x2

def main():
    print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
    a = get_float("Enter a: ", False)
    b = get_float("Enter b: ", True)
    c = get_float("Enter c: ", True)
    x1, x2 = solve_quadratic(a, b, c)
    equation = (f"{a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0"
                f" \N{RIGHTWARDS ARROW} x = {x1}")
    if x2 is not None:
        equation += f" or {x2}"
    print(equation)

main()