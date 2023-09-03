#1. Use `itertools` to create groups of similar items of a given list.
def group_BySimilar1(lst):
    # Create a dictionary to store the groups
    groups = {}

    # Group items by last name
    for element in lst:
        lastName = element.split()[-1]
        if lastName not in groups:
            groups[lastName] = []
        groups[lastName].append(element)

    return groups
"""
Noticed:
    "group" container must be dictionary of this way
    split() equivalent split(" ")

    lst = ["Thomas Brown", "Tom Smith", "Jane Brown", "John Smith"]
    
    # Convert the dictionary values to a list to get the final result
    result = list(group_BySimilar1(lst).values())
    
    print(result)
"""
from itertools import groupby
def group_BySimilar2(lst):
    # Sort the input list by last name
    lst.sort(key = lambda x: x.split()[-1]) # not clear

    groups = []
    # Use itertools.groupby to create groups based on the last name
    for key, group in groupby(lst, key = lambda x: x.split()[-1]):
        groups.append(list(group))

    return groups
"""
lst = ["Thomas Brown", "Tom Smith", "Jane Brown", "John Smith"]
print(group_BySimilar2(lst))
"""