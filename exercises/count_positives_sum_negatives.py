# Return an array, where the first element is the count of positives numbers and the second
# element is sum of negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    new_arr = []
    count = 0
    res_negative = 0
    for num in arr:
        if num > 0:
            count = count + 1
        elif num < 0:
            res_negative = res_negative + num
    new_arr.append(count)
    new_arr.append(res_negative)
    return new_arr


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([]))