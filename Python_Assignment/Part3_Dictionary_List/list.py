# Concatenate two lists index-wise
def concatenate_Lists(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append(x + y)
    return result

lst_1 = ["W", "a", "Novo"]
lst_2 = ["e", "re", "bi"]
print(concatenate_Lists(lst_1, lst_2))