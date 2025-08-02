import numpy as np

def f(x):
    return 1 / x

def boole(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("n must be a multiple of 4")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    result = 0
    for i in range(0, 4):
        result += (2 * h / 45) * (
            7 * y[i] + 32 * y[i + 1] + 12 * y[i + 2] + 32 * y[i + 3] + 7 * y[i + 4]
        )
    
    return result

a = 1
b = 2
n = 8
ans = boole(f, a, b, n)
print(f"Ans = {ans}")