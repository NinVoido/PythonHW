import numpy as np

def f(x,a):
    return a[2]*(x**2) + a[1]*x + a[0]

def integ(f, x, dx=1E-8):

    return (f(x+dx)+f(x))/2*dx

dx = 1E-4
x = 0
a = [0, 0, 1]

b = lambda x : f(x, a)

t = np.arange(0, 1, dx)

integral = 0

for i in t:
    integral += integ(b, i, dx)

print(integral)
