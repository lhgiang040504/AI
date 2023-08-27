# Map two list that key list and value list to a dictionary
def create_dictionary_from_lists(key_list, value_list):
    dct = {}
    for key, value in zip(key_list, value_list):
        dct[key] = value
    return dct

# Check multiple keys exists in a dictionary
def check_Key(dct, lst):
    for element in lst:
        if not (element in dct):
            return False
    return True

# Remove a cpecific key
def remove_Key(dct, key):
    if key in dct:
        del dct[key]
        return dict(dct)
    else:
        return "Key not found in the dictionary"

# Concatenate dictionaries
def concatenate_Dictionaries_1(*arg):
    result = {}
    for dct in arg:
        result.update(dct)
    return dict(result)
def concatenate_Dictionaries_2(*arg):
    return {k: v for dct in arg for k, v in dct.item()}
"unpacking way"

# Count number of items in a dictionary that value is a list
def count_listValuesInDictionary(dct):
    total_items = 0
    for value in dct.values():
        if isinstance(value, list):
            total_items += len(value)
    return total_items
"new** isinstance function"

# Group elements of a list based on its length:
def grouping_baseLength(lst):
    dct = {}
    for element in lst:
        length = len(element)
        if length not in dct:
            dct[length] = [element]
        else:
            dct[length].append(element)
    return dict(dct)
dct = ["the", "purpose", "of", "our", "lives", "is", "to", "be", "happy"]
print(grouping_baseLength(dct))

