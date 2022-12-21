def add(a: str, b: str) -> str:
    
    if len(a)>len(b):
        b = b.rjust(len(a),'0')
    else :
        a = a.rjust(len(b),'0')
    
    result = ''
    a = a[::-1]
    b = b[::-1]
    n = 0

    for i in range(len(a)):
        c = ord(a[i]) + ord(b[i])-96+n
        if c > 9:
            c -= 10
            n = 1
        else:
            n = 0
        result += chr(c + 48)
    
    if n == 1:
        result += '1'

    result = result[::-1]

    return result
    

