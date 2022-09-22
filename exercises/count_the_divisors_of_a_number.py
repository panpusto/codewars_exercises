# Count the number of divisors of a positive integer n.
# Random tests go up to n = 500000.


def divisors(n):
    return len([num for num in range(1, n + 1) if n % num == 0])
