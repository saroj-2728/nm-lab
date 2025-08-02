import numpy as np
import math

def f(x):
    return (math.exp(x) + math.exp(-x)) / 2

def trapezoidal(f, h, a, b):
    x = np.arange(a, b + h, h)
    n = len(x)
    y = [f(xi) for xi in x]

    sumBetweens = sum(y[i] for i in range(1, n - 1))

    return (h / 2) * (y[0] + y[-1] + 2 * sumBetweens)

def romberg(f, a, b, n):
    I = []
    h = b - a

    for i in range(n):
        hi = h / (2 ** i)
        I.append(trapezoidal(f, hi, a,  b))

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            I[j] = (4 ** i * I[j] - I[j - 1]) / (4 ** i - 1)

    return I[n - 1]

print("Enter values:")
a = float(input("a: "))
b = float(input("b: "))
n = int(input("depth: "))
ans = romberg(f, a, b, n)
print(f"Ans = {ans}")