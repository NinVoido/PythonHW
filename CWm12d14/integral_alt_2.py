def f(x: float, a):
    return a[2]*x**2 + a[1]*x + a[0]

def sqr(f, x: float, dx=1e-5):
    return f(x)*(dx)

res = 0
xsqr = [0, 0, 1]
fn = lambda x : f(x, xsqr)

curx = int(input())
stop = int(input())

while curx < stop:
    res += sqr(fn, curx)
    curx += 1e-5

print(res)
