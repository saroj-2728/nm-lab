import numpy as np
import math

def f(x):
    return math.sin(x)

def simpson13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requirees an even no. of intervals.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    sumOdds = sum(y[i] for i in range(1, n, 2))
    sumEvens = sum(y[i] for i in range(2, n, 2))

    return (h / 3) * (y[0] + y[-1] + 4 * sumOdds + 2 * sumEvens)

a = float(input("a: "))
b = float(input("b: "))
n = int(input("n: "))
ans = simpson13(f, a, b, n)
print(f"Ans = {ans}")