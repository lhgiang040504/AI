# Use filter to get the list of positive numbers
def get_PosNumbers(input):
    input = [int(element) for element in input]
    output = filter(lambda x : x > 0, input)
    return list(output)
lst = input().split(" ")
print(get_PosNumbers(lst))