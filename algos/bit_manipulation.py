
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count


def ones(k):
    num = 1
    for i in range(1, k):
        num = (num << 1) + 1
    return num


def significant_digits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count



