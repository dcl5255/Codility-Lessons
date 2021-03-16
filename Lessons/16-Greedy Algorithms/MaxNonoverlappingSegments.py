# I didn't initially see that B[K] <= B[K + 1] for all K.
# My first solution took this into account separately to make sure that
# we chose the optimal line segment.
def solution(A, B): # O(N), 100% on codility
    n = len(A)

    if n == 0:
        return 0

    count = 0
    last_ending = -1

    i = 0
    for i in range(n):
        if A[i] > last_ending:
            count += 1
            last_ending = B[i]
    return count

def first_solution(A, B): # O(N) or O(N + max(B)), 80% on codility
    n = len(A)

    if n == 0:
        return 0

    C = []

    for i in range(n):
        C.append(B[i] - A[i])

    count = 0
    last_ending = -1

    i = 0
    while i < n:
        if A[i] > last_ending:
            best_next = i
            for j in range(i + 1, n):
                if A[best_next] == A[j] and C[j] < C[best_next]:
                    best_next = j
                else:
                    i = best_next
            count += 1
            last_ending = B[i]
        i += 1
    return count


if __name__ == '__main__':
    print(solution([1, 3, 7, 9, 9, 10], [5, 6, 8, 9, 10, 11]))