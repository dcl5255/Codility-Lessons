import math

def solution(X, Y, D):
    return math.ceil((Y-X)/D)

if __name__ == '__main__':
    print(solution(10,85,30))