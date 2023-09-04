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

@login_Required
def protected_Function():
    print("Successful access")

#protected_Function()

import time
def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper
