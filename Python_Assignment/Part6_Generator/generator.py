class fibonacciGenerator:
    def __init__(self):
        self.flow = [0]

    def __next__(self):
        if len(self.flow) == 2:
            result = self.flow[0] + self.flow[1]
            self.flow.append(result)
            self.flow.pop(0)
            return result
        
        self.flow.append(1)
        return 1
"""
# Create a Fibonacci number generator
fibonacci = fibonacciGenerator()

print(next(fibonacci))  # Output: 1
print(next(fibonacci))  # Output: 1
print(next(fibonacci))  # Output: 2
print(next(fibonacci))  # Output: 3
print(next(fibonacci))  # Output: 5
print(next(fibonacci))  # Output: 8
"""

class multipleBy:
    def __init__(self, factor):
        self.curr = 0
        self.factor = factor

    def __next__(self):
        self.curr += self.factor
        return self.curr
"""
multiply = multipleBy(5)
for i in range(100):
    print(next(multiply))
"""

def exponentialBy(exponent):
    curr = 1
    while not (curr > 100):
        yield curr ** exponent
        curr += 1
"""
In the context of your exponentialBy generator, each time you call next(exponential), the generator function exponentialBy(n) calculates the next value and yields it. 
The function's state is then saved until the next iteration. 
This allows you to generate values on-the-fly without having to store them all in memory at once.
"""
exponential = exponentialBy(3)

print(next(exponential))  # Output: 1
print(next(exponential))  # Output: 8
print(next(exponential))  # Output: 27