# Concatenate two lists index-wise
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


lst_1 = ["Hello", "World"]
lst_2 = ["Dear", "Sir"]
print(following_orderConcatenate_Lists(lst_1, lst_2))

