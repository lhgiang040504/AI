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
    
dct = {"1": "value_1", "2": "value_2", "3": "value_3"}
key = 1
print(remove_Key(dct, str(key)))
