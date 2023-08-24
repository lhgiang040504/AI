import math
# Map for conversion data
"""
During "conversion," data is often changed in both value and format.
During "casting," the primary goal is to change the data type of the data while keeping the underlying value unchanged (in safe casting scenarios).
"""
# lst = input().split(" ") The format way to input a list
"""
After practice, i infer:
1) the split() function will return an array of strings;
2) map([element], [container]) that x is the action you want to each elements of your container
3) lamda is same but more flexible than map
"""
def Convers(input):
    input = [float(element) for element in input]
    output = map(math.floor, input)
    return list(output)

# Map for square  data
def Spuare(input):
    input = [int(element) for element in input]
    output = map(lambda element : element**2, input) # Can not same the abl=ove because pow need two argumants
    # Float result : math.pow(element, 2)
    return list(output)

# Map to count same pair in two container "MatchPairCount"
def PairTally(container1 , container2):
    count = sum(map(lambda x, y : 1 if x == y else 0, container1, container2))
    return count

container1 = input().split(" ")
container2 = input().split(" ")
print(PairTally(container1, container2))