def f(x: float, a):
    return a[0]*x**2 + a[1]*x + a[2]

def sqr(f, x: float, dx=1e-4):
    return f(x)*(dx)

sqr_under_fn = 0
xsqr = [1, 0, 0]
fn = lambda x : f(x, xsqr)

curx = int(input("Enter start point: "))
stop = int(input("Enter end point: "))

while curx < stop:
    sqr_under_fn += sqr(fn, curx)
    curx += 1e-4

print(sqr_under_fn)
