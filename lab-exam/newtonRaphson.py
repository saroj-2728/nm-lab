def f(x):
    return 2 * x ** 2 + 4 * x - 5

def g(x):
    return 4 * x + 4

def newtonRaphson(f, g, a, e = 1e-4, n = 100):
    i = 0
    while(True):
        if g(a) == 0:
            print("Error! First derivative = 0.")
            return None
        
        x = a - f(a)/g(a)
        a = x

        if (abs(f(a)) < e) or i >= n:
            return a

        i += 1
        
print("Enter initial guess:")
a = float(input())

ans = newtonRaphson(f, g, a)

if ans is None:
    print("Root calculation failed!")
else:
    print(f"Root = {ans}")