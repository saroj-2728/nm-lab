def lagrange(x, y, xp):
    n = len(x)

    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j!= i:
                term *= (xp - x[j]) / (x[i] - x[j])
        result += term
    
    return result

x = [30, 35, 45, 55]
y = [148, 96, 68, 34]
xp = float(input("xp: "))

ans = lagrange(x, y, xp)
print(f"Ans = {ans}")
