import numpy as np


def script(x, y, z):
    result = []
    for i in range(len(x)):
        a = x[i] ** 2
        b = y[i] ** 2
        c = np.sqrt(a + b)
        result.append(c - z)
    return result


x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = 5

print(script(x, y, z))
