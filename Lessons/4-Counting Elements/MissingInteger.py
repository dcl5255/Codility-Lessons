def solution(A):
    positive_nums = set()

    for i in A:
        if i > 0:
            positive_nums.add(i)

    for i in range(1,len(A) + 1):
        if i not in positive_nums:
            return i

    return len(A) + 1


if __name__ == '__main__':
    print(solution([1,3,6,4,1,2]))
    print(solution([1,2,3]))
    print(solution([-1,-3]))
    print(solution([-1,-3,-3,-2,-3,4,1,2]))