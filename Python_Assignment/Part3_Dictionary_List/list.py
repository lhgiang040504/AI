# Concatenate two lists with two option
def index_wiseConcatenate_Lists(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append(x + y)
    return result
def following_orderConcatenate_Lists(lst1, lst2):
    result = []
    for x in lst1:
        for y in lst2:
            result.append(x + " " + y)
    return result
"reference"

# Iterate both lists simultaneously such that `lst_1` should display item in original order and `lst_2` in reverse order
def IterateDoubleDirection(lst1, lst2):
    result = list(zip(lst1, reversed(lst2)))
    return result

# Remove empty strings from the list of strings by using `filter` function
def remove_emptyStringsMember(lst):
    result = filter(lambda x : x != "", lst)
    return list(result)
lst_1 = ["10", "20", "30", "", "40"]

print(remove_emptyStringsMember(lst_1))

