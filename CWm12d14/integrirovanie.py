from numpy import arange

def func (x, a) -> float:
    return (x**3*a[0] + x**2*a[1] + x*a[2] + a[3])

def sq (x, f, dx=1e-4) -> float:
    return (dx * (f(x) + f(dx+x))/2)

a = [1, 0, 0, 0]
f = lambda x: func(x, a)
res = 0
for i in arange(0, 1, 1e-4):
    res += sq(i, f)
print(res)
