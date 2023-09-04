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

"""
Functions in the re module:

    re.match(pattern, string): Attempts to match the pattern at the beginning of the string. 
Returns a match object if successful, or None if no match is found.
    re.search(pattern, string): Searches the entire string for a match to the pattern. 
Returns a match object if a match is found, or None if not.
    re.findall(pattern, string): Returns all non-overlapping matches as a list of strings.
    re.finditer(pattern, string): Returns an iterator yielding match objects for all non-overlapping matches.
    re.sub(pattern, replacement, string): Replaces all occurrences of the pattern in the string with the replacement string.
    re.compile(pattern): Compiles a regular expression pattern into a regex object, which can be reused for multiple searches or matches.
"""