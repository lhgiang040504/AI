class StopIteration(Exception):
    pass

class Enumerate:
    def __init__(self, container, start=0):
        self.container = container
        self.index = start
        self.iterator = iter(self.container)

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            value = next(self.iterator)
        except StopIteration: # We need to have the name except cause we use custom Enumerate
            raise StopIteration("hello")
        
        result = (self.index, value)
        self.index += 1
        return result


class Zip:
    def __init__(self, *arg):
        self.iterator = [iter(it) for it in arg]

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            result = (next(iter) for iter in self.iterator)
        except StopIteration: # We need to have the name except cause we use custom Enumerate
            raise StopIteration("hello")
        
        return tuple(result)
"""     
# Example usage
enum_iter = iter(Enumerate(["a", "b", "c"], start=2))
print(next(enum_iter))  # Output: (2, "a")
print(next(enum_iter))  # Output: (3, "b")
print(next(enum_iter))  # Output: (4, "c")
print(next(enum_iter))  # Raises StopIteration exception
""" 

zip_iter = iter(Zip(["a", "b", "c"], [1, 2, 3, 4], ["x", "y", "z"]))

print(next(zip_iter))  # Output: ("a", 1, "x")
print(next(zip_iter))  # Output: ("b", 2, "y")
print(next(zip_iter))  # Output: ("c", 3, "z")
print(next(zip_iter))  # Raises StopIteration exception

"""
Some noticed:
    At line 33:
        (next(iter) for iter in self.iterator) the generator expression
        [next(iter) for iter in self.iterator] the list comprehension

        Here's a more detailed explanation:

In both cases, self.iterator is assumed to be an iterable containing multiple iterators (e.g., a list of iterators). 
Both expressions iterate over these iterators and apply the next function to each one to get the next value. 
The primary difference lies in the outcome:

The generator expression (next(iter) for iter in self.iterator) creates an iterator (generator) that produces values on the fly as you iterate over it. 
It's memory-efficient because it doesn't create the entire list of values in memory at once. 
This is useful when you want to process the values one at a time without storing them in a list.

The list comprehension [next(iter) for iter in self.iterator] creates a list of values by iterating over all the iterators in self.iterator and immediately collecting all the values in memory. 
This can be memory-intensive if the iterators contain a large number of elements. It's suitable when you need all the values at once and want to store them in a list.

In most cases, if memory usage is not a concern and you want to work with all the values at once, the list comprehension is more straightforward. 
If you want to process values one by one without storing them all in memory, the generator expression is a better choice.
"""