def solution(A):
    A.sort(reverse=True)
    len_a = len(A)
    with_negative = A[len_a - 1] * A[len_a - 2] * A[0]
    highest_three = A[0] * A[1] * A[2]

    return max(with_negative, highest_three)