## Regular Expression
1. Write a regular expression to check whether an email address is valid or not
    - Valid email addresses must follow these rule:
        + It must have the `username@websitename.extension` format type.
        + The username can only contain letters, digits, dashes and underscores [a-z], [A-Z], [0-9], [_-]
        + The website name can only have letters and digits [a-z], [A-Z], [0-9]
        + The extension can only contain letters [a-z], [A-Z]
        + The maximum length of the extension is 3
    - Example:
        + jayson@gmail.com => True
        + jayson_123@gmail.com => True
        + jayson-54@gmail.com.vn => False

### Document
[Python Regular Expression](https://realpython.com/regex-python/)

### How to submit your exercise?
- Put your solution for all questions into file named `regex.py`
