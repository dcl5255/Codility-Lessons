def solution(A):
    # write your code in Python 3.6
    found_values = dict()
    for i in A:
        if i not in found_values:
            found_values[i] = 1
        else:
            found_values[i] = found_values[i] + 1

    for key in found_values:
        if found_values[key] % 2 == 1:
            return key