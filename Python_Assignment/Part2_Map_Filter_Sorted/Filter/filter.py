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
    output = filter(lambda x: "a" not in x, input)
    return list(output)

dict_list = [] # Initialize an empty list to store dictionaries
user_input = input().split(";")

for item in user_input:
    dct = {}
    temp1 = item.split(" ")
    
    for pair in temp1:
        temp2 = pair.split(":")
        dct[temp2[0]] = temp2[1]
    dict_list.append(dct)
print(filt_Dict(dict_list))
