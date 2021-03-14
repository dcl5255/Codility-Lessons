import math


def solution(A): # O(N) time
    best_diff = math.inf
    left_sum = 0
    right_sum = sum(A)

    for p in range(len(A)-1):
        left_sum += A[p]
        right_sum -= A[p]
        diff = abs(left_sum - right_sum)
        best_diff = min(best_diff, diff)
    return best_diff

def first_solution(A): # O(N^2) time
    best_diff = math.inf

    for p in range(1,len(A)):
        difference = abs(sum(A[:p]) - sum(A[p:]))
        best_diff = min(best_diff, difference)
    return best_diff

if __name__ == '__main__':
    print(solution([3,1,2,4,3]))
    print(solution([1,2]))
    print(solution([-1000,1000]))

