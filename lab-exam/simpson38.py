import math

def f(x):
    return math.sin(x)

def simpson38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Simpson's 3/8 rule requires a multiple of 3 no. of intervals.")
    
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    sum3 = 0
    sumRest = 0
    
    for i in range(1, n):
        if i % 3 == 0:
            sum3 += y[i]
        else:
            sumRest += y[i]

    return  (3 * h /8) * (y[0] + y[-1] + 3 * sumRest + 2 * sum3)

a = float(input("a: "))
b = float(input("b: "))
n = int(input("n: "))
ans = simpson38(f, a, b, n)
print(f"Ans = {ans}")