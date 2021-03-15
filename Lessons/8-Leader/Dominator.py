def solution(A):
    values = dict()
    n = len(A)

    for i in range(n):
        if A[i] not in values:
            values[A[i]] = 1, i
        else:
            [count, index] = values[A[i]]
            values[A[i]] = [count+1, index]

    for i in values:
        count, idx = values[i]
        if count > (n // 2):
            return idx

    return -1