# Uses DFS to find the height of a binary tree
# A Tree contains the left subtree (l), the right subtree (r), and its value (x)

# from extratypes import Tree  # library with types used in the task
from collections import deque


def solution(T):
    if T is None:
        return -1

    frontier = deque()
    max_height = 0
    frontier.append((T, 0))

    while (frontier):
        current, height = frontier.pop()
        if current == None:
            continue
        left, right = current.l, current.r

        if left == None and right == None:
            max_height = max(height, max_height)
        else:
            frontier.append((left, height + 1))
            frontier.append((right, height + 1))

    return max_height
