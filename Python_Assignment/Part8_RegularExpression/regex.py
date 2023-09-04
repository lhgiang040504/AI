import re

def is_valid_email(email):
    # Define the regular expression pattern
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    
    # Use re.match() to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
print(is_valid_email("jayson@gmail.com"))       # True
print(is_valid_email("jayson_123@gmail.com"))   # True
print(is_valid_email("jayson-54@gmail.com.vn")) # False
