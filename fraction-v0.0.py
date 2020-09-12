from numbmod import math as _m
from numbmod import xor
class fraction(object) :
    def __init__(self,d,c=1) :
        if type(d) == fraction :
            dd = d
            cc = fraction(c)
            d = (dd/cc).d
            c = (dd/cc).c
        elif type(d) == ifraction :
            if d.neg :
                dd = fraction(-(d.a*d.c+d.d),d.c)
            else :
                dd = fraction(d.a*d.c+d.d,d.c)
            if type(c) == ifraction :
                if c.neg :
                    cc = fraction(-(c.a*c.c+c.d),c.c)
                else :
                    cc = fraction(c.a*c.c+c.d,c.c)
            else :
                cc = fraction(c)
            d = (dd/cc).d
            c = (dd/cc).c
        else :
            if type(c) == fraction :
                dd = fraction(d)
                cc = c
                d = (dd/cc).d
                c = (dd/cc).c
            elif type(c) == ifraction :
                if c.neg :
                    cc = fraction(-(c.a*c.c+c.d),c.c)
                else :
                    cc = fraction(c.a*c.c+c.d,c.c)
                if type(d) == ifraction :
                    if d.neg :
                        dd = fraction(-(d.a*d.c+d.d),d.c)
                    else :
                        dd = fraction(d.a*d.c+d.d,d.c)
                else :
                    dd = fraction(d)
                d = (dd/cc).d
                c = (dd/cc).c
            elif type(d) == float or type(c) == float :
                p = 10**max(_m.decimallen(d),_m.decimallen(c))
                d *= p
                c *= p
                d = round(d)
                c = round(c)
            if d < 0 and c < 0 : # -|
                d = -d #            |
                c = -c #            |
            elif d < 0 or c < 0 : # -- Set negative fraction.
                d = -abs(d)
                c = abs(c)
            d / c # Check
            gcd = _m.prime.gcd(d,c) # Get greatest common divisor.
            d //= gcd # -|
            c //= gcd # --- Reduce fraction.
        self.d = d
        self.c = c
    def __str__(self) :
        return str(self.d) + "/" + str(self.c)
    def __repr__(self) :
        return str(self.d) + "/" + str(self.c)
    def __float__(self) :
        return self.d / self.c
    def __eq__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c) # Get least common mutiple.
        self.d *= (lcm//self.c) # --|
        other.d *= (lcm//other.c) # -- 
        return self.d == other.d
    def __gt__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c) # Get least common mutiple.
        self.d *= (lcm//self.c) # --|
        other.d *= (lcm//other.c) # -- 
        return self.d > other.d
    def __lt__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c) # Get least common mutiple.
        self.d *= (lcm//self.c) # --|
        other.d *= (lcm//other.c) # -- 
        return self.d < other.d
    def __ge__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c) # Get least common mutiple.
        self.d *= (lcm//self.c) # --|
        other.d *= (lcm//other.c) # -- 
        return self.d >= other.d
    def __le__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c) # Get least common mutiple.
        self.d *= (lcm//self.c) # --|
        other.d *= (lcm//other.c) # -- 
        return self.d <= other.d
    def __ne__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c) # Get least common mutiple.
        self.d *= (lcm//self.c) # --|
        other.d *= (lcm//other.c) # -- 
        return self.d != other.d
    def __abs__(self) :
        return fraction(abs(self.d),abs(self.c))
    def __add__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c)
        return fraction(self.d*(lcm//self.c)+other.d*(lcm//other.c),lcm)
    def __sub__(self,other) :
        lcm = _m.prime.lcm(self.c,other.c)
        return fraction(self.d*(lcm//self.c)-other.d*(lcm//other.c),lcm)
    def __mul__(self,other) :
        return fraction(self.d*other.d,self.c*other.c)
    def __truediv__(self,other) :
        return fraction(self.d*other.c,self.c*other.d)
    def __floordiv__(self,other) :
        return round(float((self/other)-((self/other)%fraction(1))))
    def __pos__(self) :
        return self * fraction(1)
    def __neg__(self) :
        return self * fraction(-1)
    def __mod__(self,other) :
        while self >= fraction(0) :
            self = self - other
        return self + other
    def __pow__(self,other,mod=None) :
        if type(mod) in [int,float,complex,fraction] :
            mod = fraction(mod)
            if type(other) == int :
                res = fraction(1)
                if _m.isnature(other) :
                    for i in range(other) :
                        res *= self
                else :
                    for i in range(other) :
                        res /= self
                res %= mod
                return res
            else :
                return pow(float(self),float(other),float(mod))
        else :
            if type(other) == int :
                res = fraction(1)
                if _m.isnature(other) :
                    for i in range(other) :
                        res *= self
                else :
                    for i in range(other) :
                        res /= self
                return res
            else :
                return pow(float(self),float(other))
    def oppo(self) :
        return fraction(self.c,self.d)
    def write(self) :
        return str(self.d).center(max(len(str(self.d)),len(str(self.c)))) + "\n" + ("-"*max(len(str(self.d)),len(str(self.c)))) + "\n" + str(self.c).center(max(len(str(self.d)),len(str(self.c))))
class ifraction(fraction) :
    def __init__(self,a,d=0,c=1,neg=False) :
        frac = fraction(a) + fraction(d,c)
        if frac < fraction(0) :
            frac = -frac
            neg = not neg
        d = frac.d
        c = frac.c
        a = d // c
        d = abs(d) % c
        self.a = a
        self.d = d
        self.c = c
        self.neg = neg
    def __str__(self) :
        return "-" * self.neg + str(self.a) + " " + str(self.d) + "/" + str(self.c)
    def __repr__(self) :
        return "-" * self.neg + str(self.a) + " " + str(self.d) + "/" + str(self.c)
    def __float__(self) :
        if self.neg :
            return -(self.a + (self.d / self.c))
        else :
            return self.a + (self.d / self.c)
    def __eq__(self,other) :
        return fraction(self) == fraction(other)
    def __gt__(self,other) :
        return fraction(self) > fraction(other)
    def __lt__(self,other) :
        return fraction(self) < fraction(other)
    def __ge__(self,other) :
        return fraction(self) >= fraction(other)
    def __le__(self,other) :
        return fraction(self) <= fraction(other)
    def __ne__(self,other) :
        return fraction(self) != fraction(other)
    def __abs__(self) :
        return ifraction(self.a,self.d,self.c)
    def __add__(self,other) :
        return ifraction(0,(fraction(self)+fraction(other)).d,(fraction(self)+fraction(other)).c)
    def __sub__(self,other) :
        return ifraction(0,(fraction(self)-fraction(other)).d,(fraction(self)-fraction(other)).c)
    def __mul__(self,other) :
        return ifraction(0,(fraction(self)*fraction(other)).d,(fraction(self)*fraction(other)).c)
    def __truediv__(self,other) :
        return ifraction(0,(fraction(self)/fraction(other)).d,(fraction(self)/fraction(other)).c)
    def __floordiv__(self,other) :
        return fraction(self.a*self.c+self.d,self.c) // fraction(other.a*other.c+other.d,other.c)
    def __pos__(self) :
        return self
    def __neg__(self) :
        self.neg = not self.neg
        return self
    def __mod__(self,other) :
        return ifraction(0,(fraction(self)%fraction(other)).d,(fraction(self)%fraction(other)).c)
    def __pow__(self,other,mod=None) :
        if type(mod) in [int,float,complex,fraction,ifraction] :
            if type(other) == int :
                return ifraction(0,pow(fraction(self),other,mod).d,pow(fraction(self),other,mod).c)
            else :
                return pow(float(self),float(other),float(mod))
        else :
            if type(other) == int :
                return ifraction(0,pow(fraction(self),other).d,pow(fraction(self),other).c)
            else :
                return pow(float(self),float(other))
    def oppo(self) :
        return ifraction(fraction(self).oppo())
    def write(self) :
        return (" "*len(str(self.a))) + str(self.d).center(max(len(str(self.d)),len(str(self.c)))) + "\n" + str(self.a) + ("-"*max(len(str(self.d)),len(str(self.c)))) + "\n" + (" "*len(str(self.a))) + str(self.c).center(max(len(str(self.d)),len(str(self.c))))
