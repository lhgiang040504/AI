# Map for conversion data
"""
During "conversion," data is often changed in both value and format.
During "casting," the primary goal is to change the data type of the data while keeping the underlying value unchanged (in safe casting scenarios).
"""
import math
def conversion(input):
    input = [float(element) for element in input]
    output = map(math.floor, input)
    return list(output)
lst = input().split(" ")
print(conversion(lst))