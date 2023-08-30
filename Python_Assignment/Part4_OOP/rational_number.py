import math

class NotIntegerError(Exception):
    pass
class ZeroDenominatorError(Exception):
    pass

class RationalNumber:
    def __init__(self, nume, deno=1):
        if not isinstance(nume, int) or not isinstance(deno, int):
            raise NotIntegerError("NotIntegerError")
        if deno == 0:
            raise ZeroDenominatorError("ZeroDenomiator")
        
        self.nume = nume
        self.deno = deno

    def simplify(self):
        gcd = math.gcd(self.nume, self.deno)
        return RationalNumber(self.nume // gcd, self.deno // gcd) # Noted that we need // to get rid of error
    
    def __str__(self):
        self = self.simplify()
        if self.deno == 1:
            return f"{self.nume}"
        else:
            return f"{self.nume} / {self.deno}"

    def __add__(self, other):
        denominator = (self.deno * other.deno)
        numerator = (self.nume * other.deno) + (self.deno * other.nume)
        return RationalNumber(numerator, denominator).simplify()
    def __sub__(self, other):
        denominator = (self.deno * other.deno)
        numerator = (self.nume * other.deno) - (self.deno * other.nume)
        return RationalNumber(numerator, denominator).simplify()
    def __mul__(self, other):
        return RationalNumber(self.nume * other.nume, self.deno * other.deno).simplify()
    def __truediv__(self, other):
        return RationalNumber(self.nume * other.deno, self.deno * other.nume).simplify()


a = RationalNumber(4, 5)
b = RationalNumber(6, 5)
print(a / b)
