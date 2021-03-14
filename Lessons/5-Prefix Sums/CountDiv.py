def solution(A, B, K): # O(1)
    first_divisible = None

    count = 0

    diff_to_next_divisible = K - A % K
    if diff_to_next_divisible == K:
        first_divisible = A
    else:
        first_divisible = A + diff_to_next_divisible

    if first_divisible <= B:
        count = ((B - first_divisible) // K) + 1

    return count

def badSolution(A,B,K): # Off by one error on edge cases
    count = ((B - A) // K)
    if A == 0:
        count += 1
    return count

def worstSolution(A, B, K): # (A-B)/K except i'm actually so stupid...
    count = 0
    first_div_found = False

    curr = A
    while curr <= B:
        if first_div_found:
            count += 1
            curr += K
        else:
            diff_to_next_divisible = K - curr % K
            if diff_to_next_divisible == K:
                count += 1
            curr += diff_to_next_divisible
            first_div_found = True

    return count


if __name__ == '__main__':
    print(solution(0, 2000000000, 1))