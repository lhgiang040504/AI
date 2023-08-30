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

    # Override +, -, *, / 
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

    # Override <, >, =
    def __lt__(self, other):
        return self.nume/self.deno < other.nume/other.deno
    def __gt__(self, other):
        return self.nume/self.deno > other.nume/other.deno
    def __eq__(self, other):
        return self.nume/self.deno == other.nume/other.deno

try:
    r1 = RationalNumber(3, "abc")  # Raises NotIntegerError
except NotIntegerError as e:
    print(e)
    
try:
    r2 = RationalNumber(2, 0)  # Raises ZeroDenominatorError
except ZeroDenominatorError as e:
    print(e)

rational1 = RationalNumber(15, 20)
simplified_rational1 = rational1.simplify()
print(simplified_rational1)  # Output: 3/4

rational2 = RationalNumber(4, 6)
print(rational2)  # Output: 2/3

rational3 = RationalNumber(5, 1)
print(rational3)  # Output: 5

result_add = RationalNumber(1, 2) + RationalNumber(1, 3)
print(result_add)  # Output: 5/6

result_sub = RationalNumber(1, 2) - RationalNumber(1, 3)
print(result_sub)  # Output: 1/6

result_mul = RationalNumber(1, 2) * RationalNumber(1, 3)
print(result_mul)  # Output: 1/6

result_div = RationalNumber(1, 2) / RationalNumber(1, 3)
print(result_div)  # Output: 3/2

print(RationalNumber(3, 7) > RationalNumber(4, 9))  # Output: False
print(RationalNumber(3, 7) < RationalNumber(4, 11))  # Output: True
print(RationalNumber(2, 4) == RationalNumber(4, 8))  # Output: True
