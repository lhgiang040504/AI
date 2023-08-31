class fibonacciGenerator:
    def __init__(self):
        self.flow = [1]

    def __next__(self):
        if len(self.flow) == 2:
            result = self.flow[0] + self.flow[1]
            self.flow.append(result)
            self.flow.pop(0)
            return result
        
        self.flow.append(1)
        return 1
    
# Create a Fibonacci number generator
fibonacci = fibonacciGenerator()

print(next(fibonacci))  # Output: 1
print(next(fibonacci))  # Output: 1
print(next(fibonacci))  # Output: 2
print(next(fibonacci))  # Output: 3
print(next(fibonacci))  # Output: 5

    