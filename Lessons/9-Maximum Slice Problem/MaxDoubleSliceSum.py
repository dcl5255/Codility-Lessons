# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(A): # O(N), 100%, https://app.codility.com/demo/results/trainingGEUK5Z-XPN/
    best_slices_ending = dict()
    best_slices_starting = dict()
    n = len(A)

    if n <= 3:
        return 0

    max_ending = 0

    for i in range(1, n - 1):
        max_ending = max(0, max_ending + A[i])
        best_slices_ending[i] = max_ending

    best_slices_ending[0] = 0
    best_slices_ending[n-1] = 0

    max_starting = 0

    for i in range(n-2, 0, -1):
        max_starting = max(0, max_starting + A[i])
        best_slices_starting[i] = max_starting

    best_slices_starting[0] = 0
    best_slices_starting[n-1] = 0
    best_max = 0

    for i in range(1, n - 1):
        best_max = max(best_max, best_slices_starting[i + 1] + best_slices_ending[i - 1])

    return best_max


def calculate_slice_sum(A, x, y, z):
    left_sum = sum(A[x + 1:y])
    right_sum = sum(A[y + 1:z])

    return left_sum + right_sum


def first_solution(A):  # Brute force algorithm, O(N^3)
    best = -math.inf
    n = len(A)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                best = max(best, calculate_slice_sum(A, i, j, k))

    return best


if __name__ == '__main__':
    # print(calculate_slice_sum([3, 2, 6, -1, 4, 5, -1, 2], 0, 3, 6))
    # print(calculate_slice_sum([3, 2, 6, -1, 4, 5, -1, 2], 0, 3, 7))
    # print(calculate_slice_sum([3, 2, 6, -1, 4, 5, -1, 2], 3, 4, 5))
    print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
