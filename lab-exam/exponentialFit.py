import numpy as np
import math

def exponentialFit(x, y):
    n = len(x)

    u = np.array([math.log(xi) for xi in x])
    v = np.array([math.log(yi) for yi in y])

    usq = u**2
    uv = u * v
    sumU = u.sum()
    sumV = v.sum()
    sumUSq = usq.sum()
    sumUV = uv.sum()

    b = (n * sumUV - sumU * sumV) / (n * sumUSq - sumU ** 2)
    a = (sumV - b * sumU) / n
    a = math.exp(a)

    return a, b

x = np.array([25, 20, 12, 9, 7, 5])
y = np.array([0.22, 0.2, 0.15, 0.13, 0.12, 0.1])

a, b = exponentialFit(x, y)
print(f"Exponential fit: y = {a} * e ^ {b}")
