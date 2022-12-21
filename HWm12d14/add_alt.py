def dig(a):
    return ord(a) - ord('0')

def ch(a):
    return chr(a + ord('0'))


def add(a: str, b: str):
    a = a.rjust(max(len(a), len(b)), '0')
    b = b.rjust(max(len(a), len(b)), '0')
    a, b = a[::-1], b[::-1]
    c = 0
    r = ''

    for i in range(len(a)):
        digit = dig(a[i]) + dig(b[i]) + c
        if digit > 9:
            c = 1
            digit -= 10
        else: c = 0
        r = ch(digit) + r
    if c == 1: r = ch(c) + r
    return r

