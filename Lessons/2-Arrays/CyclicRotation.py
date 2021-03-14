def solution(A,K):
    arr_length = len(A)
    if (arr_length == 0):
        return A
    actual_rot = K % arr_length
    ret = A[-actual_rot:] + A[:-actual_rot]
    return ret