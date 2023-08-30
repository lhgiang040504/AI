import math

class NotIntegerError(Exception):
    pass
class ZeroDenominatorError(Exception):
    pass

class RationalNumber:
    def __init__(self, nume, deno=1):
        if not (isinstance(nume, int) and isinstance(deno, int)):
            raise NotIntegerError("NotIntegerError")
        if deno == 0:
            raise ZeroDenominatorError("ZeroDenomiator")
        
        self.nume = nume
        self.deno = deno

    def simplify(self):
        gcd = math.gcd(self.nume, self.deno)
        return RationalNumber(self.nume / gcd, self.deno / gcd)
