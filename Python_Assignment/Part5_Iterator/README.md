## Iterator
1. Instead of using `enumerate` function, create your own class. It will need to return a
tuple with each iteration, with the first element in the tuple being the index (default starting
with 0), and the second element being the current element from the underlying data structure.
    - Enumerate(["a", "b", "c"], start=2)
    - enum_iter = iter(Enumerate)
    - next(enum_iter) => (2, "a")
    - next(enum_iter) => (3, "b")
    - next(enum_iter) => (4, "c")
    - next(enum_iter) => Raise StopIteration exception

2. Instead of using `zip` function, create your own class. It will need to return a
tuple with each iteration, with the same-index elements in passed iterators are paired together
    - Zip(["a", "b", "c"], [1, 2, 3, 4], ["x", "y", "z"])
    - zip_iter = iter(Zip)
    - next(zip_iter) => ("a", 1, "x")
    - next(zip_iter) => ("b", 2, "y")
    - next(zip_iter) => ("c", 3, "z")
    - next(zip_iter) => Raise StopIteration exception

### Document
[Python Iterator](https://www.programiz.com/python-programming/iterator)

### How to submit your exercise?
- Put your solution for all questions into file named `iterator.py`
