def divide(dividend, divisor):
    if divisor == 1:
        return dividend
    elif divisor == -1:
        return 0 - dividend
    count = 0
    total = 0
    negative_divisor = divisor < 0
    negative_dividend = dividend < 0
    negative_both = negative_dividend and negative_divisor
    negative_neither = not negative_dividend and not negative_divisor

    while negative_neither and total + divisor <= dividend: # +, +
        count += 1
        total = total + divisor
    while negative_divisor and not negative_both and total - divisor <= dividend: # +, -
        count -= 1
        total = total - divisor
    while negative_both and total + divisor >= dividend: # -, -
        count += 1
        total = total + divisor
    while negative_dividend and not negative_both and total - divisor >= dividend: # -, +
        count -= 1
        total = total - divisor
    return count


if __name__ == '__main__':
    # print(divide(10, 3))
    # print(divide(7, -3))
    # print(divide(0, 1))
    # print(divide(1, 1))
    # print(divide(10, -5))
    # print(divide(-10, 5))
    # print(divide(10,20))
    # print(divide(-10,20))
    # print(divide(10,-20))
    # print(divide(-10,-20))
    print(divide(-2147483648, -2))
    pass
