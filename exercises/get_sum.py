# Given two integers a and b, which can be positive or negative, find the sum of all the integers
# between and including them and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!

def get_sum(a, b):
    result = 0
    if a > b:
        for x in range(b, a+1):
            result = result + x
    elif a < b:
        for x in range(a, b+1):
            result = result + x
    elif a == b:
        result = a
    return result


print((get_sum(0, 1)))
print(get_sum(0, -1))


# ver.2


# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))
