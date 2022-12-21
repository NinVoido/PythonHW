import time
# Here I used dicts because IMO they are more "pythonic" than ord and char
_nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def _int(s: str) -> int:
    res = 0
    for (n, ch) in enumerate(s[::-1]):
        res += _nums[ch] * 10**n
    return res

def _str(i: int) -> str:
    s = ''
    while not i == 0:
        s = _char[i % 10] + s
        i //= 10
    return s

def div(a: str, b: str) -> tuple[str, str]:
    ans = ''
    offb = 0
    val = '0'
    car = ''
    while _int(a) > _int(b):
        val = a[:len(b)+offb]
        while _int(val) < _int(b):
            print(val)
            val = a[:len(b)+offb]
            ans += '0'
            offb += 1

        ans += _char[_int(val) // _int(b)]
        
        car = _str(_int(b) * (_int(val) // _int(b)))
        a = _str(_int(a[:len(car)]) - _int(car)) + a[len(car):]
        a = _str(_int(a))
            

        val = '0'
        offb = 0

    
    ans = _str(_int(ans))
    return (ans, a)
