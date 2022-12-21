class Fraction:
   
    def reduce(self):
        gcd = __import__("math").gcd(self.n, self.d)
        self.n //= gcd
        self.d //= gcd

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
            self.a = int(str(a).split(".")[1])
            self.d = 10 ** int(str(a).split(".")[1])
            self.a += int(a)*self.d
        else:
            raise TypeError

    def __str__(self) -> str:

        return f"{self.n // self.d} ({self.n - self.n // self.d * self.d}/{self.d})"

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

