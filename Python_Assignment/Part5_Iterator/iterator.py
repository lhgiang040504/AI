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
