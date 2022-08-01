# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.


def find_short(s):
    return min([len(word) for word in s.split()])


print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("lets talk about javascript the best language"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))
print(find_short("Let's travel abroad shall we"))