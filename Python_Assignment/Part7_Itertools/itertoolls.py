#1. Use `itertools` to create groups of similar items of a given list.
def group_BySimilar(lst):
    groups = {}
    for element in lst:
        lastName = element.split(" ")[-1]

        if lastName not in groups:
            groups[lastName] = []
        groups[lastName].append(element)

    return groups
"""
Noticed:
    "group" container must be dictionary of this way
"""
lst = ["Thomas Brown", "Tom Smith", "Jane Brown", "John Smith"]
print(group_BySimilar(lst))

