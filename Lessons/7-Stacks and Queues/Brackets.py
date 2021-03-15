from collections import deque


def solution(S): # O(n), 100%
    stack = deque()
    open_to_closing = dict()
    open_to_closing['('] = ')'
    open_to_closing['{'] = '}'
    open_to_closing['['] = ']'

    for i in S:
        if i in open_to_closing:
            stack.append(i)
        else:
            if stack:
                last = stack.pop()
                if i != open_to_closing[last]:
                    return 0
            else:
                return 0

    if not stack:
        return 1
    else:
        return 0