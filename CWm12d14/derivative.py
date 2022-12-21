import numpy as np

def func(x: int, a):
    return a[0] * x**2 + a[1] * x + a[2]

def integ(f, x, dx):
    return ((f(x) + f(x + dx)) / 2) * dx

a = [1, 0, 0]
f1 = lambda x: func(x, a)
fsum = 0

vals = np.arange(0, 1, 1E-5)

for i in vals:
    fsum += integ(f1, i, 1E-5)

print(fsum)
