# def is_isogram(string):
#     upper_string = string.upper()
#     for item in upper_string:
#         if upper_string.count(item) > 1:
#             return False
#     return True


def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))
