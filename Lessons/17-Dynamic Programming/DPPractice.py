import math


# How many coins from denominations C do we need to sum up to our target k?
def dynamic_coin_changing_fulldp(C, k):  # (n*k) time, O(n*k) space
    n = len(C)

    dp = [[0 for i in range(k + 1)] for i in range(n + 1)]
    dp[0] = [0] + [math.inf] * k

    for i in range(1, n + 1):
        for j in range(C[i - 1]):
            dp[i][j] = dp[i - 1][j]
        for j in range(C[i - 1], k + 1):
            dp[i][j] = min(dp[i][j - C[i - 1]] + 1, dp[i - 1][j])

    return dp[n][k]


def dynamic_coin_changing(C, k):  # Only keeps the last row (all we're using). O(n*k) time, O(k) space
    n = len(C)
    dp = [0] + [math.inf] * k

    for i in range(1, n + 1):
        for j in range(C[i - 1], k + 1):
            dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])

    return dp[k]


# Returns the number of ways that a frog could jump from position 0 to positions 0 through k
def frog(S, k):
    n = len(S)
    dp = [1] + [0] * k
    for i in range(1, k + 1):
        for j in range(n):
            if S[j] <= i:
                dp[i] += dp[i - S[j]]
    return dp


if __name__ == '__main__':
    print(dynamic_coin_changing_fulldp([1, 3, 4], 54))
    print(dynamic_coin_changing([1, 3, 4], 54))

    print(frog([1, 2, 3], 25))
