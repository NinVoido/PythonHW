# n = 20
#
# l = []
# for i in range(n):
#     l.append(i ** 2)
#
# l = [i ** 2 for i in range(n)]
# print(l)
#
#
# def squares(n):
#     for i in range(n):
#         yield i**2
#
# for i in squares(n):
#     print(i)
#
# l=[]
# l.extend(squares(n))


def fibonacci(n):
    if n >= 1:
        yield 1
    if n >= 2:
        yield 1
    x1 = 1;
    x2 = 1
    for k in range(3, n + 1):
        x1 = x1 + x2
        yield x1
        x1, x2 = x2, x1


def binomNewton(n):
    C = 1
    yield C
    for k in range(1, n):
        C *= n - k + 1
        C //= k
        yield C
    yield 1


roman1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
roman2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
roman3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

def to_roman(n):
    if n == 0:
        return 'N'
    if n < 0 or n >= 10000:
        return None
    I = n % 10
    X = (n // 10) % 10
    C = (n // 100) % 10
    M = (n // 1000) % 10
    ans = ''
    if M > 0:
        ans += 'M' * M
    if C > 0:
        ans += roman3[C]
    if X > 0:
        ans += roman2[X]
    if I > 0:
        ans += roman1[I]
    return ans


def romanRange(start, stop=None, step=None):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1
    for i in range(start, stop, step):
        yield to_roman(i)
