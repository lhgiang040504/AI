# Check palindrome
def is_palindrome(string):
    string = string.lower().replace(" ", "") # Convert the passed string to lover case and remove space but for each purpose
    return string == string[::-1] # The method to slicing string, list, ... Explain: [start:end:step]
"""
string = str(input())
print(is_palindrome(string))
"""

# Filter the element that have same remainder after the division with passed num
def collect_commonRemander(lst, num):
    result = [[] for _ in range(num)] # _ is the conventional placeholder in python  This construct is often used as a starting point for populating each inner list with data as needed.
    for element in lst:
        result[(int(element) % num) - 1].append(element) # -1 is to satify the ouput format
    return result
"""
lst = list(input().split(" "))
num = int(input())
print(collect_commonRemander(lst, num))
"""

# Split a string into a list of word
def tokenize_byWord(string):
    result = []
    result = string.split(" ")
    return result
"""
string = str(input())
print(tokenize_byWord(string))
"""

# Count sum by a dfunction that take a variable number of argument
def Sum(*arg):
    total = sum(arg)
    return total
"""
print(Sum(1, 2))
"""

# Default information
def initialize_employee(name = "", gender = None, salary = 0):
    employee = {
        "name": name,
        "gender": gender,
        "salary" : salary
    }
    return employee

employee = initialize_employee("Sahra")
for key, value in employee.items():
    # print("{}: {}".format(key, value))
    print(f"{key}: {value}")