import math


def is_square(n):
    if n < 0:
        return False

    root = math.sqrt(n)

    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False


print(is_square(4))
print(is_square(6))

