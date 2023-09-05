from functools import wraps
def login_Required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        attemps = 3
        while attemps > 0:
            user_name = input("Enter user name: ")
            user_pass = input("Enter user pass: ")
            if user_name == "1" and user_pass == "1":
                print("Login successful")
                return func(*args, **kwargs) # need
            else:
                print(f"Login failed. {attemps - 1} attemps left")
                attemps -= 1
        print("You have exceeced the maximum number of login attemps.")
    return wrapper # not
"""
use *args and **kwargs :
Flexibility:
By using *args and **kwargs, the decorator can be applied to functions with varying numbers of positional and keyword arguments. 
It makes the wrapper function flexible and capable of forwarding any arguments provided to the original function.

Compatibility:
It ensures that the wrapper function can work with any function that it decorates without needing to know the specific signature of those functions in advance.

Pass-Through Behavior:
In many cases, you may want to pass any arguments and keyword arguments from the decorated function to the original function to ensure that the decorated function behaves similarly to the original one.
"""
@login_Required
def protected_Function():
    print("Successful access")

#protected_Function()

import time
def measure_ExecutionTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@measure_ExecutionTime
def some_function():
    # Your code here
    time.sleep(2)  # Simulate some work

#some_function()

def bold_Decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}<b>"
    return wrapper
def italic_Decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}<i>"
        pass
    return wrapper
def underline_Decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}<u>"
    return wrapper

@bold_Decorator
@italic_Decorator
@underline_Decorator
def func(text):
    return text
"""
text = "hello everyone"
result = func(text)
print(result)
"""

def decor1(func):
    @wraps(func)
    def wrapper():
        result = func()
        return result ** 2
    return wrapper

def decor2(func):
    @wraps(func)
    def wrapper():
        result = func()
        return result * 2
    return wrapper

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
