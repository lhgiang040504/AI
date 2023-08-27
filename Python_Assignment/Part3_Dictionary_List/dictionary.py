# Map two list that key list and value list to a dictionary
def create_dictionary_from_lists(key_list, value_list):
    dct = {}
    for key, value in zip(key_list, value_list):
        dct[key] = value
    return dct

key_list = input().split(" ")
value_list = map(int, input().split(" "))
print(create_dictionary_from_lists(key_list, value_list))