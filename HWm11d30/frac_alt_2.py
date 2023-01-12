from math import gcd

class Fraction:
   
    def reduce(self):
        ggcd = gcd(self.n, self.d)
        self.n //= ggcd
        self.d //= ggcd

    def __init__(self, a, b=None, c=None):
        if isinstance(a, int):
            if b == None:
                self.n = a
                self.d = 1
            elif isinstance(b, int):
                if c == None:
                    self.n = a
                    self.d = b
                else:
                    self.n = b
                    self.n += a*c
                    self.d = c
        elif isinstance(a, str):
            a = a.replace("/", " ")
            a = a.replace("(", "")
            a = a.replace(")", "")
            ops = list(map(int, a.split()))
            self.n = ops[1]
            self.n += ops[0]*ops[2]
            self.d = ops[2]
        elif isinstance(a, Fraction):
            self.n = a.n
            self.d = a.d
        elif isinstance(a, float):
            self.n = int(str(a).split(".")[1])
            self.d = 10 ** len(str(a).split(".")[1])
            self.n += int(a)*self.d
        
        self.reduce()

    def __str__(self) -> str:

        return f"целое:{self.n // self.d} остальное:({self.n - self.n // self.d * self.d}/{self.d})"

    def __add__(self, sec):
        temp = self
        if isinstance(sec, int):
                temp.n += sec*temp.d
        elif isinstance(sec, Fraction):
                temp.n *= sec.d
                temp.n += sec.n * temp.d
                temp.d *= sec.d
        
        temp.reduce()
        
        return temp

    def __sub__(self, sec):
        temp = self
        if isinstance(sec, int):
                temp.n -= sec*temp.d
        elif isinstance(sec, Fraction):
                temp.n *= sec.d
                temp.n -= sec.n * temp.d
                temp.d *= sec.d
        
        temp.reduce()
    
        return temp

    def __mul__(self, sec):
        temp = self
        if isinstance(sec, int):
                temp.n *= sec
        elif isinstance(sec, Fraction):
                temp.n *= sec.n
                temp.d *= sec.d
        
        temp.reduce()
        
        return temp
    
    def __truediv__(self, sec):
        temp = self         
        if isinstance(sec, int):
                temp.d *= sec
        elif isinstance(sec, Fraction):
                temp.d *= sec.n
                temp.n *= sec.d
        
        temp.reduce()
        
        return temp

def try_into(a : str) :
    if "." in a:
        try:
            return float(a)
        except:
            pass
    else:
        try:
            return int(a)
        except:
            return a



f = Fraction(0)

print("""Available commands: =, +, -, *, /
examples:
    = 1.5
    + 1""")
while True:
    c = input().split()
    match c[0]:
        case "=":
            f = eval(f"Fraction({try_into(c[1])})")
        case "+":
            f += eval(f"Fraction({try_into(c[1])})")
        case "-":
            f -= eval(f"Fraction({try_into(c[1])})")
        case "*":
            f *= eval(f"Fraction({try_into(c[1])})")
        case "/":
            f /= eval(f"Fraction({try_into(c[2])})")
    print(f)

