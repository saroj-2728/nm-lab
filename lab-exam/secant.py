def f(x):
    return x ** 3 - 4 * x - 9

def secant(f, a, b, e = 1e-5, n = 100):
    for i in range(n):
        denominator = f(b) - f(a)
        if denominator == 0:
            print("Error! Denominator 0.")
            return None
        
        x = (a * f(b) - b * f(a)) / denominator
        if abs(f(x)) < e:
            return x

        a = b
        b = x
    
    print("Max iterations reached without convergence.")
    return None

print("Enter initial guesses:")
a = float(input())
b = float(input())

root = secant(f, a, b)
if root is None:
    print("Root calculation failed!")
else:
    print(f"Root = {root}")