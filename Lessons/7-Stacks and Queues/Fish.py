from collections import deque

def solution(A, B): # O(N), 100%
    up_stream = deque()
    down_stream = deque()

    for i in range(len(A)):
        if B[i] == 1:
            down_stream.append(A[i])
        else:
            survived = True
            while down_stream:
                last_fish = down_stream.pop()
                if last_fish > A[i]:
                    down_stream.append(last_fish)
                    survived = False
                    break
            if survived:
                up_stream.append(A[i])

    return len(up_stream) + len(down_stream)