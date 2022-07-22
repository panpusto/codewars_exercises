# Complete the function that accepts a string parameter, and reverses each word in
# the string. All spaces in the string should be retained.
# Examples
#
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


# def reverse_words(text):
#     arr = []
#     separate_text = text.split()
#     for item in separate_text:
#         arr.append(item[::-1])
#
#     return ' '.join(arr)


def reverse_words(text):
    return ' '.join([item[::-1] for item in text.split(' ')])


print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('apple'))
print(reverse_words('a b c d'))
print(reverse_words('double  spaced  words'))


