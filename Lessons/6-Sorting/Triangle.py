def solution(A): #O(nlogn), 100%, https://app.codility.com/demo/results/trainingJFCVJ7-Z5V/
    a_len = len(A)
    A.sort()

    if a_len < 3:
        return 0

    for i in range(a_len - 2):
        if A[i] > 0 and (A[i] + A[i+1] > A[i+2]):
            return 1
    return 0


def brute_force_solution(A): #brute force solution, O(n^3), 75%
    a_len = len(A)

    if a_len < 3:
        return 0

    for i in range(a_len):
        for j in range(i + 1, a_len):
            for k in range(j + 1, a_len):
                if A[i] + A[j] > A[k] and A[j] + A[k] > A[i] and A[k] + A[i] > A[j]:
                    return 1
    return 0


if __name__ == '__main__':
    print(solution([10,2,5,1,8,20]))
    print(solution([10,50,5,1]))
    print(solution([]))
    print(solution([1]))
    print(solution([1,2]))
    print(solution([3,4,5]))