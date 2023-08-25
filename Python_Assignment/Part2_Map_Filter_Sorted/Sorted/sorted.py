# Sort in descending order
"sort need integer"
def descending_Sort(lst):
    lst = [int(element) for element in lst]
    return sorted(lst)

lst = input().split(" ")
print(descending_Sort(lst))
