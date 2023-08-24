# Use filter to get the list of positive numbers
def get_PosNumbers(input):
    input = [int(element) for element in input]
    output = filter(lambda x : x > 0, input)
    return list(output)

# Use filter to collect words that has first letter is capital
def initial_capsWord(input):
    output = filter(lambda x : x[0].isupper(), input)
    return list(output)
lst = input().split(" ")
print(initial_capsWord(lst))