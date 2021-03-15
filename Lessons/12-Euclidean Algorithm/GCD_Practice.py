def gcd_subtraction(a, b):
    if a == b:
        return a
    if a > b:
        return gcd_subtraction(a - b, b)
    else:
        return gcd_subtraction(a, b - a)


def gcd_division(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_division(b, a % b)


# Codility's binary Euclidean Algorithm
def gcd(a, b, res=1):
    if a == b:
        return res * a
    elif a % 2 == 0 and b % 2 == 0:
        return gcd(a // 2, b // 2, 2 * res)
    elif a % 2 == 0:
        return gcd(a // 2, b, res)
    elif b % 2 == 0:
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)


def lcm(a,b):
    return (a * b) / gcd(a, b, 1)


if __name__ == '__main__':
    print(gcd_subtraction(20, 5))
    print(gcd_division(20, 5))
    print(gcd(20, 5))
    print(lcm(20, 5))
