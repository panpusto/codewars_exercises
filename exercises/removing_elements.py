# Take an array and remove every second element from the array.
# Always keep the first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!


#   1st solution
def remove_every_other(my_list):
    return [item for item in my_list if my_list.index(item) % 2 == 0]

#   2nd solution
# def remove_every_other(my_list):
#     return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([[1, 2]]))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
