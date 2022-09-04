# The maximum sum subarray problem consists in finding the maximum sum of a contiguous
# subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum
# sum is the sum of the whole array. If the list is made up of only negative
# numbers, return 0 instead.
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    list_of_sum = []
    for elem in arr:
        for idx in range(arr.index(elem) + 1, len(arr)):
            elem += arr[idx]
            list_of_sum.append(elem)
            print(elem)

    if all(i < 0 for i in arr) or not list_of_sum:
        return 0

    else:
        max_sum = max(list_of_sum)
        return max_sum


print(max_sequence([]))    # => 0
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # => 6
