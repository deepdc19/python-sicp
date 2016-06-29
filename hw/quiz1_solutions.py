#  Name:
#  Email:

# Q1.

def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True
    >>> [overlaps(a0, b0, a1, b1) for a0, b0, a1, b1 in 
    ...       ( (1, 4, 2, 3), (1, 4, 0, 2), (1, 4, 3, 5), (0.1, 0.4, 0.2, 0.3),
    ...         (2, 3, 1, 4), (0, 2, 1, 4), (3, 5, 1, 4) )].count(False)
    0
    >>> [overlaps(a0, b0, a1, b1) for a0, b0, a1, b1 in 
    ...       ( (1, 4, -1, 0), (1, 4, 5, 6), (1, 4, 4, 5), (1, 4, 0, 1),
    ...         (-1, 0, 1, 4), (5, 6, 1, 4), (4, 5, 1, 4), (0, 1, 1, 4),
    ...         (5, 5, 3, 6), (5, 3, 4, 6), (5, 5, 5, 5), 
    ...         (3, 6, 5, 5), (4, 6, 5, 3), (0.3, 0.6, 0.5, 0.5) )].count(True)
    0
    """
    return low1 < min(high0, high1) > low0

# Q2.

def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1
    >>> cases = [(1, 0), (2, 1), (3, 1), (4, 1), (5, 4), (6, 4), 
    ...          (10, 9), (17, 16), (26, 25), (36, 25), (46, 36)]
    >>> [last_square(s) == t for s, t in cases].count(False)
    0
    """
    k = 0
    while k * k < x:
        k = k + 1
    return (k-1) * (k-1)

# Q3.

def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    >>> cases = [(1, True), (9, True), (10, False), (11, True), (32, False),
    ...          (23, True), (99, True), (111, True), (122, True), (223, True),
    ...          (232, False), (999, True),
    ...          (13334566666889, True), (987654321, False)]
    >>> [ordered_digits(s) == t for s, t in cases].count(False)
    0
    """
    last = x % 10
    val = x // 10
    while x > 0 and last >= x % 10:
        last = x % 10
        x = x // 10
    return x == 0

