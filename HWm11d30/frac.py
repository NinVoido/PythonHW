class Fraction:
   
    def reduce(self):
        gcd = __import__("math").gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    def __init__(self, num: int, den=1):
        self.num = num
        self.den = den
        self.reduce()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __add__(self, sec):
        
        if isinstance(sec, int):
                self.num += sec*self.den
        elif isinstance(sec, Fraction):
                self.num *= sec.den
                self.num += sec.num * self.den
                self.den *= sec.den
        
        self.reduce()
        
        return self

    def __sub__(self, sec):
        
        if isinstance(sec, int):
                self.num -= sec*self.den
        elif isinstance(sec, Fraction):
                self.num *= sec.den
                self.num -= sec.num * self.den
                self.den *= sec.den
        
        self.reduce()
        
        return self

    def __mul__(self, sec):
        
        if isinstance(sec, int):
                self.num *= sec
        elif isinstance(sec, Fraction):
                self.num *= sec.num
                self.den *= sec.den
        
        self.reduce()
        
        return self

    def __truediv__(self, sec):
        
        if isinstance(sec, int):
                self.den *= sec
        elif isinstance(sec, Fraction):
                self.den *= sec.num
                self.num *= sec.den
        
        self.reduce()
        
        return self

num = int(input("Input a numerator: "))
den = int(input("Input a denumerator: "))

frac = Fraction(num, den)

print(frac)
print(f"{frac} + 2 = {frac + 2}")
print(f"{frac} * 1/2 = {frac * Fraction(1, 2)}")
print(f"{frac} / 3/5 = {frac / Fraction(3, 5)}") 
