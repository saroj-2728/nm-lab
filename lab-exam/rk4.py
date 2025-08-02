def f(x, y):
    return y - x

def rk4(f, x0, y0, xp, h):
    n = int((xp - x0) / h)

    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)

        y0 += (1 / 6) * (k1 + 2 * (k2 + k3) + k4)
        x0 += h

    return y0

print("Enter the values: ")
a = float(input("x0: "))
b = float(input("y(x0): "))
h = float(input("h: "))
xp = float(input("xp: "))
ans = rk4(f, a, b, xp, h)
print(f"Ans = {ans}")