## OOP
1. Create abstract class `Shape` with methods:
    - `calculate_perimeter()`
    - `calculate_area()`
2. Create child class `Rectangle`, inherited from class `Shape`:
    - Attribute:
        + `height`
        + `width`
    - Re-define method `calculate_perimeter()`and `calculate_area()` with correct expression
        + Rectangle(3, 6).calculate_perimeter() = 16
        + Rectangle(3, 6).calculate_area() = 15
3. Create child class `Square`, inherited from class `Shape`:
    - Attribute:
        + `side`
    - Re-define method `calculate_perimeter()`and `calculate_area()` with correct expression
        + Square(5).calculate_perimeter() = 20
        + Square(5).calculate_area() = 25
4. Create child class `Triangle`, inherited from class `Shape`:
    - Attribute:
        + `sides`
    - Re-define method `calculate_perimeter()`and `calculate_area()` with correct expression
        + Triangle((3, 4, 5)).calculate_perimeter() = 12
        + Triangle((3, 4, 5)).calculate_area() = 6

5. Create class `RationalNumber` with attributes:
    - `numerator`
    - `denominator`, default = 1
6. Write exception hierarchy which defines a different exception for each of these error conditions
(when creating `RationalNumber` objects):
    - Numerator or Denominator is not an integer -> Raise NotIntegerError
    - Denominator = 0 -> Raise ZeroDenominatorError
    *Hint: Inherit from class Exception* 
7. Create method `simplify()` to simplify the retional number:
    - RationalNumber(15, 20).simplify() = 3/4
8. Override `__str__()` method to display the `RationalNumber` object when it is represented as a string
    - print(RationalNumber(4, 6)) => 2/3
    - print(RationalNumber(5, 1)) => 5
9. Override `__add__()`, `__sub__()`, `__mul__()` and `__div__()` methods to perform arithmetic with rational numbers
    - RationalNumber(1, 2) + RationalNumber(1, 3) => 5/6
    - RationalNumber(1, 2) - RationalNumber(1, 3) => 1/6
    - RationalNumber(1, 2) * RationalNumber(1, 3) => 1/6
    - RationalNumber(1, 2) / RationalNumber(1, 3) => 3/2
10. Override `__lt__()`, `__gt__()` and `__eq__()` methods to perform comparison with rational numbers
    - RationalNumber(3, 7) > RationalNumber(4, 9) => False
    - RationalNumber(3, 7) < RationalNumber(4, 11) => True
    - RationalNumber(2, 4) = RationalNumber(4, 8) => True

### Document
[Python OOP](https://realpython.com/python3-object-oriented-programming/)

### How to submit your exercise?
- Put your solution for questions 1-4 into file named `shape.py`
- Put your solution for questions 5-10 into file named `rational_number.py`
