def solution(A): #no dp to start off...
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return abs(A[0])

    S = [1]

    total = A[0]

    for i in range(1,n):
        if abs(total + A[i]) < abs(total - A[i]):
            S.append(1)
            total += A[i]
        else:
            S.append(-1)
            total -= A[i]

    return abs(total), S

def solution(A): # Codility's 'slow' solution
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return abs(A[0])

    for i in range(len(A)):
        A[i] = abs(A[i])

    S = sum(A)
    dp = [0] * (S + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(S, -1, -1):
            if dp[j] == 1 and j + A[i] <= S:
                dp[j + A[i]] = 1
    result = S

    for i in range( (S // 2) + 1):
        if dp[i] == 1:
            result = min(result, S - 2*i)
            if result == 0:
                return 0
    return result


if __name__ == '__main__':
    print(solution([1,5,2,-2]))




