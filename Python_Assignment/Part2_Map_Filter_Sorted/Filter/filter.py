# Use filter to get the list of positive numbers
def get_PosNumbers(input):
    input = [int(element) for element in input]
    output = filter(lambda x : x > 0, input)
    return list(output)

# Use filter to collect words that has first letter is capital
def initial_capsWord(input):
    output = filter(lambda x : x[0].isupper(), input)
    return list(output)

# Use filter to get dict that hasnot specific key or value 
def filt_Dict(input):
    output = filter((lambda x : "a" not in x ), input)
    return list(output)

dict_list = [] # Initialize an empty list to store dictionaries
while True: # Loop to continuously input dictionaries
    key = input()
    value = input()
    
    # Check if the user wants to stop
    if key.lower() == 'stop':
        break
    
    # Create a dictionary using the input
    user_dict = {key: value}
    dict_list.append(user_dict)

print(filt_Dict(dict_list))