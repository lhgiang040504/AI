import math
# Map for conversion data
"""
During "conversion," data is often changed in both value and format.
During "casting," the primary goal is to change the data type of the data while keeping the underlying value unchanged (in safe casting scenarios).
"""
def Convers(input):
    input = [float(element) for element in input]
    output = map(math.floor, input)
    return list(output)

def Spuare(input):
    input = [int(element) for element in input]
    output = map(lambda element : int(math.pow(element, 2)), input) # Can not same the abl=ove because pow need two argumants
    return list(output)

lst = input().split(" ") # The format way to input a list
print(Spuare(lst))