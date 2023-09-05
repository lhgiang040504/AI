## Partial Function
1. Write the decorator, let the user enter the user name, password, and give the user
three chances before each execution of the decorated function. After the login is
successful, the function can be accessed.

2. Write a decorator to evaluate the execution time of a function

3. Write a chain of function decorators (bold, italic, underline)

4. Write `decor1` and `decor2` decorators to make `num_a()` and `num_b()` run correctly
```
@decor1
@decor2
def num_a():
    return 10

@decor2
@decor1
def num_b():
    return 10

print(num_a())
print(num_b())
```
    - Output: 400 200
    - Hint:
        + `decor1` do exponential operation between the return value of function and a constant
        + `decor2` do multiplication operation between the return value of function and a constant

### Document
[Python Decorator](https://realpython.com/primer-on-python-decorators/)

### How to submit your exercise?
- Put your solution for all questions into file named `decorator.py`
