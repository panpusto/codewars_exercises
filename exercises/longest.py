# Take 2 strings s1 and s2 including only letters from ato z.
# Return a new sorted string, the longest possible, containing distinct
# letters - each taken only once - coming from s1 or s2.
#
# Examples:
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    a1_list = [x for x in a1]
    a2_list = [y for y in a2]
    full_list = set(a1_list + a2_list)
    return ''.join(sorted(full_list))

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
