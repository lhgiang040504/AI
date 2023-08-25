# Sort in descending order
"sort need integer"
def descending_Sort(lst):
    lst = [int(element) for element in lst]
    return sorted(lst, reverse=True)
"""
Note that:
    numbers = [5, 2, 9, 1, 5]
    result = numbers.sort()
    print(result)  # Output: None
    print(numbers)  # Output: [1, 2, 5, 5, 9]
"""
# Reverse the order
def reverse_Order(lst):
    return lst[::-1]

lst = input().split(" ")
print(reverse_Order(lst))

"""
Note that:
    format of each type of value is not same that may cause error
"""