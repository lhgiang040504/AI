from functools import partial

def multiply(y, x):
    return x * y

# Define partial functions using functools.partial
doubleNum = partial(multiply, x=2)
tripleNum = partial(multiply, x=3)

# Test the partial functions
result1 = doubleNum(5)
result2 = tripleNum(5)

print(result1)  # Output: 10 (5 * 2)
print(result2)  # Output: 15 (5 * 3)

"""
In this code:

We import the partial function from the functools module.

We define the multiply() function as you provided.

We use functools.partial to create new functions doubleNum and tripleNum that are partially applied versions of multiply. 
We specify the y argument as a fixed value of 2 for doubleNum and 3 for tripleNum.

We then use these partial functions to calculate the double and triple of a number, as shown in the test cases.

By using functools.partial, you create specialized functions that are derived from a more general function, making your code more modular and concise.
"""