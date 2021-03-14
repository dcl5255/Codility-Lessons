# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A) + 1
    expected_sum = n * (n + 1) // 2

    for i in A:
        expected_sum -= i

    return expected_sum


def sorted_solution(A):
    if len(A) == 0:
        return 1

    sorted_arr = sorted(A)
    lastNum = None
    for i in sorted_arr:
        if lastNum is not None:
            if lastNum + 1 != i:
                return lastNum + 1
        lastNum = i

    if len(A) + 1 in sorted_arr:
        return 1
    else:
        return len(A) + 1


if __name__ == '__main__':
    print(sorted_solution([2, 3, 1, 5]))
    print(sorted_solution([1]))
    print(sorted_solution([1, 3]))
    print(sorted_solution([]))
    print()
    print(sorted_solution([2,3,4,5]))
    print(sorted_solution([1, 3, 4, 5]))
    print(sorted_solution([1, 2, 4, 5]))
    print(sorted_solution([1, 2, 3, 5]))
    print(sorted_solution([1, 2, 3, 4]))
