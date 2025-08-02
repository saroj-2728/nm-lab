import math

def f(x):
    return math.sin(x) - 1/x

def bisection(f, a, b, e, n = 1000):
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses!")
        return None
    
    i = 0
    while(True):
        x = (a + b)/2

        if f(x) < 0:
            a = x
        else:
            b = x

        if (abs(f(x)) < e) or i >= n:
            return x
        
        i += 1

print("Enter initial guesses: ")
a = float(input())
b = float(input())

ans = bisection(f, a, b, 1e-5, 100)

if ans == None:
    print("Root calculation failed!")
else:
    print(f"Root: {ans}")

            