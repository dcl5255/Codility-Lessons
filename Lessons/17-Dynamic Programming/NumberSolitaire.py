import math

def solution(A): # O(N), 100%
    n = len(A)
    dp = [A[0]] + [0] * (n - 1) # Solve using dp, storing the maximum value we need to get to each array index

    for i in range(1, n):
        highest = -math.inf
        for j in range(i - 6, i):
            if j < 0:
                continue
            highest = max(highest, dp[j] + A[i])
        dp[i] = highest

    return dp[-1]


if __name__ == '__main__':
    print(solution([1, -2, 0, 9, -1, -2]))
    print(solution([5,20,-15,3]))