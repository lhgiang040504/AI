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

#2. Use `itertools` to combine two lists into a new list
from itertools import chain
def combine_List(lst_1, lst_2):
    # Combine the lists using itertools.chain
    return list(chain(lst_1, lst_2))
# Before combine, we need extract the nested list
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
"""
# Input lists
lst_1 = [["We", "are"], "Novobi"]
lst_2 = ["We", ["are", "Novobi"]]
lst_1 = flatten_list(lst_1)
lst_2 = flatten_list(lst_2)
# Print the combined list
print(combine_List(lst_1, lst_2))
"""

#3. Use `itertools` to generate unique combinations
def combine_Unique1(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append(f"{lst[i]} - {lst[j]}")
    return result
from itertools import combinations
def combine_Unique2(lst):
    # Generate unique combinations of 2 elements
    unique_combinations = list(combinations(lst, 2))

    # Format the combinations as strings
    return [" - ".join(combination) for combination in unique_combinations]
"""
# unique_combinations = [f"{a} - {b}" for i, a in enumerate(input_list) for j, b in enumerate(input_list) if i < j]

combination
permutation

print(combine_Unique2(["Red", "Yellow", "Green"]))
"""

#4. Use `itertools` to group all iterables together and produce a single iterable
def combine_List1(*arg):
    # Combine the lists using itertools.chain
    return list(chain(*arg))
def combine_List2(*arg):
    result = []
    for lst in arg:
        result.extend(lst)
    return result
"""
lst_1 = [1, 4, 7, 10, 13, 16]
lst_2 = [2, 5, 8, 11, 14, 17]
lst_3 = [3, 6, 9, 12, 15, 18]

print(combine_List2(lst_1, lst_2, lst_3))
"""

#5. Use `itertools` to display elements in an iterable in the group of length
def combine_ByLength(lst):
    lst.sort(key = lambda x: len(x))

    groups = {}
    # Use itertools.groupby to create groups based on the last name
    for key, group in groupby(lst, key = lambda x: len(x)):
        groups[key] = list(group)
    return dict(groups)

lst = ["keep", "smiling", "because", "life",
        "is", "a", "beautiful", "thing",
          "and", "there", "is", "so",
            "much", "to", "smile", "about"]
result = combine_ByLength(lst)
for key, group in result.items():
    print(f"Key: {key} - Group: {group}")
