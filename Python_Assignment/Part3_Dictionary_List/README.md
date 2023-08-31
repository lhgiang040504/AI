## Dictionary
1. Map two lists into a dictionary:
    - Input:
        + `keys` = ["key_1", "key_2", "key_3"]
        + `values` = ["value_1", "value_2", "value_3"]
    - Output: dictionary = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}

2. Check multiple keys exists in a dictionary:
    - Input:
        + `dictionary` = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
        + `lst_1` = ["key_1", "key_4"]
        + `lst_2` = ["key_2", "key_3"]
    - Output:
        + Check `lst_1` => False
        + Check `lst_2` => True

3. Remove a key from a dictionary:
    - Input:
        + `dictionary` = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
        + `key` = "key_1"
    - Output:
        + dictionary = {"key_2": "value_2", "key_3": "value_3"}

4. Concatenate dictionaries to create a new one
    - Input:
        + `dict_1`: {1: 10, 2: 20}
        + `dict_2`: {3: 30, 4: 40}
        + `dict_3`: {5: 50, 6: 60}
    - Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

5. Count number of items in a dictionary that value is a list
    - Input: {"key_1": ["value_1", "value_2"], "key_2": ["value_3", "value_4", "value_5"]}
    - Output: 5

6. Group elements of a list based on its length:
    - Input: ["the", "purpose", "of", "our", "lives", "is", "to", "be", "happy"]
    - Output: {
        3: [ "the", "our" ],
        7: [ "purpose" ],
        2: [ "of", "is", "to", "be" ],
        5: [ "lives", "happy" ]
    }

## List
1. Concatenate two lists index-wise:
    - Input:
        + `lst_1` = ["W", "a", "Novo"]
        + `lst_2` = ["e", "re", "bi"]
    - Output: `lst` = ["We", "are", "Novobi"]

2. Concatenate two lists in the following order:
    - Input:
        + `lst_1` = ["Hello", "World"]
        + `lst_2` = ["Dear", "Sir"]
    - Output: lst = ["Hello Dear", "Hello Sir", "World Dear", "World Sir"]

3. Iterate both lists simultaneously such that `lst_1` should display item in original order and `lst_2` in reverse order:
    - Input:
        + `lst_1` = [10, 20, 30]
        + `lst_2` = [100, 200, 300]
    - Output: lst = [(10, 300), (20, 200), (30, 100)]

4. Remove empty strings from the list of strings by using `filter` function:
    - Input: ["10", "20", "30", "", "40"]
    - Output: ["10", "20", "30", "40"]

5. Remove all occurrence of 20 from the list by using list comprehension:
    - Input: ["10", "20", "30", "40", "20", "50"]
    - Output: ["10", "20", "40", "50"]

6. Sort a list of dictionaries
    - Input: [
        {"make": "Nokia", "model": 216, "color": "Black"},
        {"make": "Mi Max", "model": 2, "color": "Gold"},
        {"make": "Samsung", "model": 7, "color": "Blue"}
    ]
    - Output: [
        {"make": "Nokia", "model": 216, "color": "Black"},
        {"make": "Samsung", "model": 7, "color": "Blue"},
        {"make": "Mi Max", "model": 2, "color": "Gold"}
    ]

### Document
[Dictionary](https://www.geeksforgeeks.org/python-dictionary/)
[List](https://www.geeksforgeeks.org/advanced-python-list-methods-and-techniques/)

### How to submit your exercise?
- Put your solution for section `Dictionary` into file named `dictionary.py`
- Put your solution for section `List` into file named `list.py`
