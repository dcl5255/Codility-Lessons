def solution(A): # O(n) according to codility, still looks like O(NlogN) to me. 100% on codility
    n = len(A)
    best_profit = 0
    lowest_start = 200001

    for i in range(n):
        if A[i] >= lowest_start:
            continue
        lowest_start = A[i]

        for j in range(i + 1, n):
            best_profit = max(A[j] - A[i], best_profit)

    return best_profit

def first_solution(A): # Brute Force, O(N*logN), Codility says O(N^2)

    n = len(A)
    best_profit = 0

    for i in range(n):
        for j in range(i+1, n):
            best_profit = max(A[j] - A[i], best_profit)

    return best_profit

