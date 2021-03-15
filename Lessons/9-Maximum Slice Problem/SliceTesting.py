def quadratic_max_slice(A):
    n = len(A)
    result = 0
    for i in range(n):
        summed = 0
        for j in range(i, n):
            summed += A[j]
            result = max(summed, result)

    return result


def golden_max_slice(A):
    max_ending, max_slice = 0, 0

    for i in A:
        max_ending = max(0, max_ending + i)
        max_slice = max(max_slice, max_ending)
    return max_slice


if __name__ == '__main__':
    print(quadratic_max_slice([5, -7, 3, 5, -2, 4, -1]))
    print(golden_max_slice([5, -7, 3, 5, -2, 4, -1]))
