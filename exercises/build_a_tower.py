# Build a pyramid-shaped tower given a positive integer number of floors.
# A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]

def tower_builder(n_floor):
    result = []
    width = (n_floor * 2) - 1
    for x in range(1, 2*n_floor, 2):
        stars = x * '*'
        line = stars.center(width)
        result.append(line)
    return result


print(tower_builder(5))