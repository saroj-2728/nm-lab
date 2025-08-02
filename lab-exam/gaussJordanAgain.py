import numpy as np

def gaussJordan(A, B):
    A = A.astype(float)
    B = B.astype(float)
    n = len(A)

    Aug = np.hstack([A, B.reshape(-1, 1)])
    for i in range(n):
        pivot = Aug[i][i]
        if pivot == 0:
            raise ValueError("Error! Pivot 0.")
        
        Aug[i] = Aug[i] / pivot
        for j in range(n):
            if i != j:
                factor = Aug[j][i]
                Aug[j] = Aug[j] - factor * Aug[i]
        
    return  Aug[:, -1]

A = np.array([
    [20, 1, -2],
    [3, 20, -1],
    [2, -3, 20]
])
B = np.array([17, -18, 25])

solution = gaussJordan(A, B)
print(f"Solution: \n{solution}")