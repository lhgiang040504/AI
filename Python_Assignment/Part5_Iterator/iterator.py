class StopIteration(Exception):
    pass

class Enumerate:
    def __init__(self, container, start=0):
        self.container = container
        self.start = start
        self.iterator = iter(self.container)

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            value = next(self.iterator)
        except StopIteration: # We need to have the name except cause we use custom Exception
            raise StopIteration
        
        result = (self.start, value)
        self.start += 1
        return result

# Example usage
enum_iter = iter(Enumerate(["a", "b", "c"], start=2))
print(next(enum_iter))  # Output: (2, "a")
print(next(enum_iter))  # Output: (3, "b")
print(next(enum_iter))  # Output: (4, "c")
print(next(enum_iter))  # Raises StopIteration exception