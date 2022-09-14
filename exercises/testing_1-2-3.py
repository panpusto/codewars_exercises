# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
# Examples: (Input --> Output)
# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]


# def number(lines):
#     length = len(lines)
#     output = []
#     for i in range(length):
#         output.append(f'{i + 1}: {lines[i]}')
#     return output

# more pythonic way
def number(lines):
    return [f"{i + 1}: {lines[i]}" for i in range(len(lines))]


print(number([]))   # => []
print(number(["a", "b", "c"]))    # => ["1: a", "2: b", "3: c"]
