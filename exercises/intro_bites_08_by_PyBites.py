# In this Bite you calculate the total amount of points earned with Ninja Belts
# by accessing the given ninja_belts dict.
#
# You learn how to access score and ninjas (= amount of belt owners) from
# no less than a namedtuple (if you're new to them, check out the basic Point example in the docs).
#
# Why a namedtuple, you did not even mention a tuple yet?!
#
# Good point, well in our Bites we might actually use them even more so let's
# get to know them here (if you have a free evening read up on the collections module as well and thank us later).
#
# The function returns the total score int. You learn to write generic
# code because we test for an updated ninja_belts dict as well, see the TESTS tab.


from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
    total_result = 0
    for key, value in belts.items():
        total_result += (value[0] * value[1])
    return total_result


# tests for this exercise in tests.py
