# def reverseseq(n):
#     return list(range(n, 0, -1))


def reverseseq(n):
    array = []
    array.append(n)
    num_elem = n
    while len(array) < num_elem:
        n -= 1
        array.append(n)
    return array


print(reverseseq(5))

