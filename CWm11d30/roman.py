roman1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
roman2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
roman3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

roman_values = (('I',1), ('IV',4), ('V',5), ('IX',9),('X',10),('XL',40),('L',50),('XC',90),('C',100),
                    ('CD', 400), ('D', 500), ('CM', 900), ('M',1000))

def from_roman(roman):
    total=0
    for symbol,value in reversed(roman_values):
        while roman.startswith(symbol):
            total += value
            roman = roman[len(symbol):]
    return total

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

class Rom:
    def __init__(self, num) -> None:
        if isinstance(num, int):
            self.n = num
        elif isinstance(num, Rom):
            self = num
        elif isinstance(num, str):
            try:
                self.n = from_roman(num)
            except:
                print("String is not valid roman")
                raise TypeError
        else:
            raise TypeError
        
    def __add__(self, other):
        if isinstance(other, int):
            return Rom(self.n + other)
        elif isinstance(other, Rom):
            return Rom(self.n + other.n)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, int):
            return Rom(self.n - other)
        elif isinstance(other, Rom):
            return Rom(self.n - other.n)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return Rom(self.n * other)
        elif isinstance(other, Rom):
            return Rom(self.n * other.n)
        else:
            raise TypeError

    def __truediv__(self, other):
        try:
            if isinstance(other, int):
                return Rom(self.n // other)
            elif isinstance(other, Rom):
                return Rom(self.n // other.n)
            else:
                raise TypeError
        except:
            print("Dividing by 0 is not allowed")
            raise ArithmeticError
    
    def __str__(self):
        return to_roman(self.n)


