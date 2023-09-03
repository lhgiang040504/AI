## Itertools
1. Use `itertools` to create groups of similar items of a given list.
    - Input: ["Thomas Brown", "Tom Smith", "Jane Brown", "John Smith"]
    - Output: [["Thomas Brown", "Jane Brown"], ["Tom Smith", "John Smith"]]

2. Use `itertools` to combine two lists into a new list
    - Input:
        + `lst_1` = [["We", "are"], "Novobi"]
        + `lst_2` = ["We", ["are", "Novobi"]]
    - Output: ["We", "are", "Novobi", "We", "are", "Novobi"]

3. Use `itertools` to generate unique combinations
    - Input: ["Red", "Yellow", "Green"]
    - Output: ["Red - Yellow", "Red - Green", "Yellow - Green"]

4. Use `itertools` to group all iterables together and produce a single iterable
    - Input:
        + `lst_1` = [1, 4, 7, 10, 13, 16]
        + `lst_2` = [2, 5, 8, 11, 14, 17]
        + `lst_3` = [3, 6, 9, 12, 15, 18]
    - Output:
        + [1, 4, 7, 10, 13, 16, 2, 5, 8, 11, 14, 17, 3, 6, 9, 12, 15, 18]

5. Use `itertools` to display elements in an iterable in the group of length
    - Input: ["keep", "smiling", "because", "life", "is", "a", "beautiful", "thing", "and", "there", "is", "so", "much", "to", "smile", "about"]
    - Output:
        + Key: 1 - Group: [ "a" ]
        + Key: 2 - Group: [ "is", "is", "so", "to" ]
        + Key: 3 - Group: [ "and" ]
        + Key: 4 - Group: [ "keep", "life", "much" ]
        + Key: 5 - Group: [ "thing", "there", "smile", "about" ]
        + Key: 7 - Group: [ "smiling", "because" ]
        + Key: 9 - Group: [ "beautiful" ] 

### Document
[Python Itertools](https://realpython.com/python-itertools/)

### How to submit your exercise?
- Put your solution for all questions into file named `itertools.py`
