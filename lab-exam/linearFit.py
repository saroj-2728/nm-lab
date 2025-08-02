import numpy as np

def linearFit(x, y):
    n = len(x)

    xy = x * y
    xsq = x ** 2
    sumX = x.sum()
    sumY = y.sum()
    sumXY = xy.sum()
    sumXSq = xsq.sum()

    b = (n * sumXY - sumX * sumY) / (n * sumXSq - sumX**2)
    a = (sumY - b * sumX) / n

    return a, b

x = np.array([6, 7, 7, 8, 8, 8, 9, 9, 10])
y = np.array([5, 5, 4, 5, 4, 3, 4, 3, 3])

a, b = linearFit(x, y)
print(f"Linear fit: y = {a} + {b}x")