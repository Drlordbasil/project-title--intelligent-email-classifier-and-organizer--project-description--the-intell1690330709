import numpy as np


def script(x, y, z):
    return np.sqrt(np.array(x)**2 + np.array(y)**2) - z


x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = 5

print(script(x, y, z))
