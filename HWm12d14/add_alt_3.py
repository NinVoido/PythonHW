def digit(a):
    return ord(a) - ord('0')

def char(a: int):
    return chr(a + ord('0'))

def add(a: str, b: str) -> str:
    if len(a) < len(b): a, b = b, a
    carry = 0
    res = ''
    for i in range(len(a)):
        try:
            dig = digit(a[-(i+1)]) + digit(b[-(i+1)])
        except:
            dig = digit(a[-(i+1)])
        dig += carry
        if dig > 9:
            carry = 1
            dig -= 10
        else:
            carry = 0
        res = char(dig) + res

    return res

