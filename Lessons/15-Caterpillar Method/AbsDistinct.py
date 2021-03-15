def solution(A):
    abs_values = set()

    n = len(A)

    for i in A:
        val = abs(i)
        if val not in abs_values:
            abs_values.add(val)

    count = 0
    for i in abs_values:
        count += 1

    return count


if __name__ == '__main__':
    print(solution([-5, -3, -1, 0, 3, 6]))