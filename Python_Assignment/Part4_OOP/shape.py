from abc import ABC, abstractmethod
import math

class Shape:
    def __init__(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass
  
class Rectangle(Shape):
    def __init__(self, a, b):
        self.length = a
        self.width = b
    def calculate_perimeter(self):
        return (self.length + self.width)*2
    def calculate_area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, a):
        self.Edge = a
    def calculate_perimeter(self):
        return 4 * self.Edge
    def calculate_area(self):
        return self.Edge * self.Edge


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.aEdge = a
        self.bEdge = b
        self.cEdge = c
    def calculate_perimeter(self): 
        return self.aEdge + self.bEdge + self.cEdge
    def calculate_area(self):
        p = self.calculate_perimeter()
        temp = (p - self.aEdge)*(p - self.bEdge)*(p - self.cEdge)
        return math.sqrt(p * temp)
# Creating instances of shapes
rectangle = Rectangle(5, 10)
square = Square(7)
triangle = Triangle(3, 4, 5)

# Calculating and printing areas
print(rectangle.calculate_area())
print(square.calculate_area())
print(triangle.calculate_area())