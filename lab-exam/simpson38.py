import numpy as np
import math

def f(x):
    return math.sin(x)

def simpson38(f, x):
    n = len(x)
    if (n - 1) % 3 != 0:
        raise ValueError("Simpson's 3/8 rule requires a multiple of 3 no. of intervals.")
    
    h = x[1] - x[0]

    y = [f(xi) for xi in x]

    sum3 = sum(y[i] for i in range(1, n - 1) if i % 3 == 0)
    sumRest = sum(y[i] for i in range(1, n - 1) if i % 3 != 0)

    return  (3 * h /8) * (y[0] + y[-1] + 3 * sumRest + 2 * sum3)

x = np.array([xi * math.pi / 18 for xi in range(10)])
ans = simpson38(f, x)
print(f"Ans = {ans}")