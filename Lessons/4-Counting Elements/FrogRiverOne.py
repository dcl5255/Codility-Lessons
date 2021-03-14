import math


def solution(X, A):
    leave_times = dict()
    for i in range(len(A)):
        if A[i] <= X:
            if A[i] not in leave_times:
                leave_times[A[i]] = i

    min_time = -math.inf
    for i in range(1, X + 1):
        if i not in leave_times:
            return -1
        else:
            min_time = max(leave_times[i], min_time)
    return min_time


if __name__ == '__main__':
    print(solution(5, [1,3,1,4,2,3,5,4]))
    print(solution(5, [1,3,4,2,2,3,1,4]))
    print(solution(1,[2]))

