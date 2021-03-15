
def solution(A): # Instead, let's use a set to try to do this in O(N)
    values = set()
    for i in A:
        values.add(i)

    count = 0
    for i in values:
        count += 1

    return count


def sorting_solution(A): # O(Nlog(N)), 100%, Codility obviously wants a solution that uses sorting, so let's try that first
    A.sort()

    count = 0

    for i in range(0, len(A)):
        if i == 0:
            count += 1
        elif A[i] > A[i - 1]:
            count += 1

    return count


if __name__ == '__main__':
    print(solution([2,1,1,2,3,1]))