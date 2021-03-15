import math


def solution(A): # Only receives a 66% on Codility, need to improve this
    n = len(A)

    if n < 3:
        return 0

    peaks = []

    for i in range(1, n - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)

    peak_count = len(peaks)

    if peak_count == 1:
        return 1

    best_flag_count = 0

    for k in range(0, peak_count + 1):
        last_flag = -math.inf
        flag_count = k
        for x in range(peak_count):
            if flag_count == 0:
                break
            if peaks[x] - last_flag >= k:
                last_flag = peaks[x]
                flag_count -= 1
        if flag_count == 0:
            best_flag_count = max(best_flag_count, k)

    return best_flag_count


if __name__ == '__main__':
    print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
    print(solution([0,0,0,0,0,0,0,0]))
    print(solution([1,2,1,2,1,2,1,2,1,2]))
    print(solution([1,3,2]))
    print(solution([1,3,2,5,4]))
