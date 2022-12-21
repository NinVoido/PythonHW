from math import gcd

class Fraction:
    def __init__(self, a, b=None, c=None):
        if isinstance(a, int):
            if b == None:
                    self.num = a
                    self.denum = 1
            else:
                if c == None:
                    self.num = a
                    self.denum = b
                else:
                    self.num = b
                    self.denum = c
                    self.num += a*self.denum
        elif isinstance(a, str):
            a = a.replace("/", " ").replace("(", "").replace(")", "")
            a = a.split()
            self.num = int(a[1])
            self.denum = int(a[2])
            self.num += int(a[0])*self.denum
        elif isinstance(a, Fraction):
            self.num = a.num
            self.denum = a.denum
        elif isinstance(a, float):
            self.denum = 10**len(str(a).split(".")[1])
            self.num = int(str(a).split(".")[1])
            self.num += int(a)*self.denum
        
        self.nice()

    def nice(self):
        red_by = gcd(self.num, self.denum)
        self.num //= red_by
        self.denum //= red_by 
        
    def __add__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return Fraction(self.num*sec.denum + sec.num*self.denum, self.denum*sec.denum)

    def __sub__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return Fraction(self.num*sec.denum - sec.num*self.denum, self.denum*sec.denum)

    def __mul__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return Fraction(self.num*sec.num, self.denum*sec.denum)

    def __truediv__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return Fraction(self.num*sec.denum, self.denum*sec.num)

    def __eq__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return self.num == sec.num and self.denum == sec.denum

    def __lt__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return self.num*sec.denum < sec.num*self.denum

    def __gt__(self, sec):
        if not isinstance(sec, Fraction):
             sec = Fraction(sec)
        return self.num*sec.denum > sec.num*self.denum
    
    def __le__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return self < sec or self == sec

    def __ge__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return self > sec or self == sec

    def __ne__(self, sec):
        if not isinstance(sec, Fraction):
            sec = Fraction(sec)
        return not self == sec
    
    def __float__(self):
        return self.num / self.denum

    def __str__(self):
        res = ""
        tmp = Fraction(self)
        if self.denum <= self.num:
            res += str(self.num // self.denum)
            tmp.num -= (self.num // self.denum)*self.denum
        res += f"({tmp.num}/{tmp.denum})={float(self)}"
        return res

def true_var(fr):
    ops = fr.split()
    if len(ops) == 2:
        return Fraction(int(ops[0]), int(ops[1]))
    elif len(ops) == 3:
        return Fraction(int(ops[0]), int(ops[1]), int(ops[2]))
    elif len(ops) == 1:
        if "." in fr:
            try:
                return Fraction(float(fr)) 
            except:
                pass
        else:
            try: return Fraction(int(fr))
            except: return Fraction(fr)
frac = Fraction(0)
is_comp = False

while True:
    com = input().split(maxsplit=1)
    fr2 = true_var(com[1])
    match com[0]:
        case "=":
            frac = fr2 
        case "+":
            frac += fr2 
        case "-":
            frac -= fr2 
        case "*":
            frac *= fr2 
        case "/":
            frac /= fr2
        case "==":
            print(fr2 == frac)
            is_comp = True
        case "<":
            print(fr2 > frac)
            is_comp = True
        case ">":
            print(fr2 < frac)
            is_comp = True
        case ">=":
            print(fr2 <= frac)
            is_comp = True
        case "<=":
            print(fr2 >= frac)
            is_comp = True
        case "!=":
            print(fr2 != frac)
            is_comp = True
        case _:
            print("Unknown command, try again")
            continue

    if not is_comp:
        print(frac)

    is_comp = False
