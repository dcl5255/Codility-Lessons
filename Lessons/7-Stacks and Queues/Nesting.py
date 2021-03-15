def solution(S):
    count = 0

    for i in S:
        if i == '(':
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                return 0

    if count == 0:
        return 1
    else:
        return 0