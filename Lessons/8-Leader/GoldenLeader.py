from collections import deque

# Returns the leader of an array, that is, the element which occurs in more than half of the array
# This is a modified version of codility's solution to this
def golden_leader(A):
    stack = deque()

    for i in A:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] != i:
                stack.pop()
            else:
                stack.append(i)

    leader = -1

    if stack:
        leader = stack[-1]

    count = 0
    for i in A:
        if i == leader:
            count += 1

    if count > len(A) // 2:
        return leader
    else:
        return -1


# My own implementation of the leader problem. Should also be done in O(N).
def my_golden_leader(A):
    values = dict()
    n = len(A)

    for i in A:
        if i not in values:
            values[i] = 1
        else:
            values[i] += 1

    for i in values:
        if values[i] > (n // 2):
            return i

    return -1



if __name__ == '__main__':
    print(golden_leader([4,6,6,6,6,8,8]))
    print(my_golden_leader([4,6,6,6,6,8,8]))
    print(golden_leader([4, 6, 6, 6, 3, 8, 8]))
    print(my_golden_leader([4, 6, 6, 6, 3, 8, 8]))