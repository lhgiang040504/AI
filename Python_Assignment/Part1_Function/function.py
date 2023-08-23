# Check palindrome
def is_palindrome(string):
    string = string.lower().replace(" ", "") # Convert the passed string to lover case and remove space but for each purpose
    return string == string[::-1] # The method to slicing string, list, ... Explain: [start:end:step]

string = input()
print(is_palindrome(string))