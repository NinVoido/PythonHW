def add(a: str, b: str) -> str:
    if len(a) < len(b): a, b = b, a
    carry = 0
    res = ''
    for i in range(len(a)):
        try:
            dig = ord(a[-(i+1)]) + ord(b[-(i+1)]) - ord('0')*2
        except:
            dig = ord(a[-(i+1)]) - ord('0')
        dig += carry
        if dig > 9:
            carry = 1
            dig -= 10
        else:
            carry = 0
        res = chr(dig + ord('0')) + res
    
    if carry:
        res = '1' + res
    return res

a = input()
b = input()
print(add(a, b))
