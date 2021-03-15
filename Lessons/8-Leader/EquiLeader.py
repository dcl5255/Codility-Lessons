def my_golden_leader(A):
    values = dict()
    n = len(A)

    for i in A:
        if i not in values:
            values[i] = 1
        else:
            values[i] += 1

    for i in values:
        if values[i] > (n // 2):
            return i

    return -1


def solution(A):  # Brute force, O(n^2), calculate leader for each split, https://app.codility.com/demo/results/trainingQS2X2X-EE6/
    n = len(A)
    count = 0
    if n <= 1:
        return 0

    for i in range(1, len(A)):
        left = A[:i]
        right = A[i:]

        left_leader = my_golden_leader(left)
        right_leader = my_golden_leader(right)

        if left_leader == right_leader and left_leader != -1:
            count += 1

    return count
