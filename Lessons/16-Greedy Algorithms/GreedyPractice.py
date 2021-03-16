from collections import deque


# M contains each denomination of a coin
def greedy_coin_changing(M, k):
    n = len(M)
    result = []
    for i in range(n - 1, -1, -1):
        result += [(M[i], k // M[i])]
        k %= M[i]
    return result


def greedy_canoeist1(W, k):
    n = len(W)
    skinny = deque()
    fatso = deque()

    for i in range(n - 1):
        if W[i] + W[-1] <= k:
            skinny.append(W[i])
        else:
            fatso.append(W[i])
    fatso.append(W[-1])

    canoes = 0
    while skinny or fatso:
        if len(skinny) > 0:
            skinny.pop()
        fatso.pop()
        canoes += 1
        if not fatso and skinny:
            fatso.append(skinny.pop())
        while len(fatso) > 1 and fatso[-1] + fatso[0] <= k:
            skinny.append(fatso.popleft())

    return canoes


def greedy_canoeist2(W, k):
    canoes = 0
    j = 0
    i = len(W) - 1
    while i >= j:
        if W[i] + W[j] <= k:
            j += 1
        canoes += 1
        i -= 1
    return canoes


if __name__ == '__main__':
    print(greedy_coin_changing([1, 2, 5], 33))
    print(greedy_coin_changing([1, 5, 10, 25], 334))
    print(greedy_coin_changing([1, 3, 4], 6))  # Not an optimal solution

    print(greedy_canoeist1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
    print(greedy_canoeist2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
