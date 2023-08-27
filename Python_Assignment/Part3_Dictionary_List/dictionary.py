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
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
print(concatenate_Dictionaries_1(dict_1, dict_2, dict_3))

