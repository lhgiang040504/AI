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

dct = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
lst1 = ["key_1", "key_4"]
lst2 = ["key_2", "key_3"]
print(check_Key(dct, lst1))
print(check_Key(dct, lst2))