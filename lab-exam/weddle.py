def f(x):
    return 1 / x

def weddle(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("n must be a multiple of 6")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    result = 0
    for i in range(0, n, 6):
        result += (
            y[i] + 5 * y[i + 1] + y[i + 2] + 6 * y[i + 3] + y[i + 4] + 5 * y[i + 5] + y[i + 6]
        )
    
    return result * (3 * h / 10)

a = 1
b = 2
n = 12

ans = weddle(f, a, b, n)
print(f"Ans = {ans}")