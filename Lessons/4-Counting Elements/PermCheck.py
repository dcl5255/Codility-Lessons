def solution(A):
    encountered = set()
    N = len(A)

    for i in A:
        if i in encountered or i > N:
            return 0
        encountered.add(i)

    for i in range(1, len(A) + 1):
        if i not in encountered:
            return 0

    return 1