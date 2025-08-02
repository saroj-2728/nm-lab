import numpy as np

def f(x):
    return 1 / x

def simpson13(f, x):
    n = len(x)
    if (n - 1) % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requirees an even no. of intervals (odd no. of points).")

    h = x[1] - x[0]

    y = [f(xi) for xi in x]

    sumOdd = sum(y[i]  for i in range(1,  n-1, 2))
    sumEven = sum(y[i] for i in range(2, n-2, 2))

    result = (h/3) * (y[0] + y[-1] + 4 * sumOdd + 2 * sumEven)
    return result

x = np.array([16, 19, 21, 22, 20, 17, 13, 11, 9])
ans = simpson13(f, x)
print(f"Ans = {ans}")