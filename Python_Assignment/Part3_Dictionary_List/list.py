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

# Remove all occurrence of 20 from the list by using list comprehension
# my basic
def basic(lst):
    result = []
    for x in lst:
        if x == "20" and x in result:
            continue
        result.append(x)
    return result


# Sort a list of dictionary based on the specific key
def sortListDict_baseKey(lst):
    return sorted(lst , key = lambda k : k['model'], reverse=True)
lst_1 = [
        {"make": "Nokia", "model": 216, "color": "Black"},
        {"make": "Mi Max", "model": 2, "color": "Gold"},
        {"make": "Samsung", "model": 7, "color": "Blue"}
    ]

print(sortListDict_baseKey(lst_1))

