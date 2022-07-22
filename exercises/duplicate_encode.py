# The goal of this exercise is to convert a string to a new string where each character in the
# new string is "(" if that character appears only once in the original string, or ")" if
# that character appears more than once in the original string. Ignore capitalization when determining
# if a character is a duplicate.

def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(char) == 1 else ')' for char in word])


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))

# word = word.upper()
# result = ""
# for char in word:
#     if word.count(char) > 1:
#         result += ")"
#     else:
#         result += "("
#
# return result


# def duplicate_encode(word):
#     new_string = ""
#     word = word.lower()
#
#     for char in word:
#         new_string += (")" if (word.count(char) > 1) else "(")
#
#     return new_string