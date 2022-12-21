import numpy as np

def f(x, a):
    return a[0]*x*x + a[1]*x + a[2]

# Метод средних прямоугольников
def integ(f, x, dx=1e-4):
    return f((x+x+dx)/2)*dx

a = [1, 0, 0]

custom_fn = lambda x : f(x, a)

ssum = 0

for i in np.arange(0, 1, 1e-4):
    ssum += integ(custom_fn, i)

print(ssum)
