# Write a function that will return the count of distinct case-insensitive alphabetic
# characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    arr = [item.lower() for item in text]
    new_arr = []
    for char in arr:
        count_char = arr.count(char)
        if count_char > 1 and char not in new_arr:
            new_arr.append(char)

    return len(new_arr)


print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))


# def duplicate_count(s):
#     return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
