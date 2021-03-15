# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    rounded_root = math.ceil(N ** (1/2))
    count = 0

    for i in range(1, rounded_root):
        if N % i == 0:
            count += 2

    if (rounded_root * rounded_root) == N:
        count += 1

    return count


if __name__ == '__main__':
    print(solution(24))