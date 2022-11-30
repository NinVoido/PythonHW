import generators_2;


_rdecode = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))

def decode( roman ):
    result = 0
    for r, r1 in zip(roman, roman[1:]):
        rd, rd1 = _rdecode[r], _rdecode[r1]
        result += -rd if rd < rd1 else rd
    return result + _rdecode[roman[-1]]

class Roman(int):
    def __new__(cls, num):
        if isinstance(num, str):
            return super(cls, cls).__new__(cls, decode(num))
        else:
            return super(cls, cls).__new__(cls, num)

    def __add__(self, other):
        tmp = super(Roman, self).__add__(other)
        return self.__class__(tmp) 

    def __sub__(self, other):
        tmp = super(Roman, self).__sub__(other)
        return self.__class__(tmp) 
    
    def __mul__(self, other):
        tmp = super(Roman, self).__mul__(other)
        return self.__class__(tmp) 

    @staticmethod
    def to_roman(n):
        return generators_2.to_roman(n)

    def __str__(self):
        return Roman.to_roman(self)


