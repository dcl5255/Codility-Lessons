from collections import deque

def block_size_possible(A, K, mid):
    sum = 0
    blocks = 0

    for i in A:
        if sum + i > mid:
            sum = i
            blocks += 1
        else:
            sum += i
        if blocks >= K:
            return False
    return True

def solution(K, M, A): # O(N * log(N+M))
    minimum = max(A)
    maximum = sum(A)
    result = maximum

    while(minimum <= maximum):
        mid = (minimum + maximum) // 2
        if block_size_possible(A, K, mid):
            maximum = mid - 1
            result = mid
        else:
            minimum = mid + 1

    return result



def solution(K, M, A):
    n = len(A)
    if n <= 3:
        return max(A)

    t = n // K
    lists = []
    sums = []

    for i in range(K):
        new_list = None

        if i == K - 1:
            new_list = deque(A[i * t:])
        else:
            new_list = deque(A[i * t:(i + 1) * t])

        lists.append(new_list)
        sums.append(sum(new_list))

    max_sum = max(sums)

    for i in range(len(lists)):
        if i != 0:
            i

    return t

    pass


if __name__ == '__main__':
    print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))
