def solution(N, A):  # O(N+M)
    counters = [0] * N
    max_counter = 0
    last_max = 0
    for i in A:
        if i <= N:
            counters[i - 1] = max(counters[i - 1], last_max)
            counters[i - 1] += 1
            max_counter = max(counters[i - 1], max_counter)
        else:
            last_max = max_counter

    for i in range(len(counters)):
        counters[i] = max(counters[i], last_max)
    return counters


def first_solution(N, A):  # O(N+M)... too slow
    counters = [0] * N
    max_counter = 0
    for i in A:
        if i <= N:
            counters[i - 1] += 1
            max_counter = max(counters[i - 1], max_counter)
        else:
            counters = [max_counter] * N
    return counters


def worse_solution(N, A):  # O(N*M) :/
    counters = [0] * N
    max_counter = 0
    for i in A:
        if i <= N:
            counters[i - 1] += 1
            max_counter = max(counters[i - 1], max_counter)
        else:
            for x in range(N):
                if counters[x] != max_counter:
                    counters[x] = max_counter
    return counters


if __name__ == '__main__':
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
    print(solution(1, [2]))
    print(solution(2, [2, 2, 2, 3, 1, 1, 1, 1]))

    print(first_solution(5, [3, 4, 4, 6, 1, 4, 4]))
    print(first_solution(1, [2]))
    print(first_solution(2, [2, 2, 2, 3, 1, 1, 1, 1]))
