
def ranged_binary_search(arr, l, r, low, high):
    if r >= l:
        mid = l + (r - l) // 2
        if low <= arr[mid] <= high:
            return mid
        elif arr[mid] > high:
            return ranged_binary_search(arr, l, mid - 1, low, high)
        else:
            return ranged_binary_search(arr, mid + 1, r, low, high)
    else:
        return -1

# Uses modified binary search
def solution(S, P, Q): # O(N + M)
    impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    ret = []

    a_set = []
    c_set = []
    g_set = []
    t_set = []

    m = len(P)

    for ch in range(len(S)):
        if S[ch] == 'A':
            a_set.append(ch)
        elif S[ch] == 'C':
            c_set.append(ch)
        elif S[ch] == 'G':
            g_set.append(ch)
        else:
            t_set.append(ch)

    for k in range(m):
        start = P[k]
        end = Q[k]

        if ranged_binary_search(a_set, 0, len(a_set) - 1, start, end) != -1:
            ret.append(1)
        elif ranged_binary_search(c_set, 0, len(c_set) - 1, start, end) != -1:
            ret.append(2)
        elif ranged_binary_search(g_set, 0, len(g_set) - 1, start, end) != -1:
            ret.append(3)
        else:
            ret.append(4)
    return ret


def first_solution(S, P, Q): # O(N * M) https://app.codility.com/demo/results/trainingNZV4BK-VW3/
    impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    m = len(P)
    ret = []

    for k in range(m):
        start = P[k]
        end = Q[k]
        lowest_val = 4

        for j in range(start, end + 1):
            lowest_val = min(lowest_val, impact_factors[S[j]])
            if lowest_val == 1:
                break
        ret.append(lowest_val)
    return ret


if __name__ == '__main__':
    pass