import math


def divisors(n):  # O(sqrt(N)) algorithm to find all divisors of some number n
    count = 0
    root = n ** (1 / 2)
    for i in range(1, math.ceil(root)):
        if n % i == 0:
            count += 2

    if (root * root) == n:
        count += 1

    return count


def is_prime(n):
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


# There are n coins and n people. Person i turns over coin x if x is a multiple of i.
# How many coins are turned over in the end?
def coins(n):
    coin = [0] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        for k in range(i, n + 1, i):
            coin[k] = (coin[k] + 1) % 2

        result += coin[i]

    return result


if __name__ == '__main__':
    print(divisors(24))
    print(is_prime(68749))
    print(coins(10))
