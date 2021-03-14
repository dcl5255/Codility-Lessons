def solution(A): # O(N), 100% on codility
    going_east = []
    going_west = []

    for i in range(len(A)):
        if A[i] == 0:
            going_east.append(i)
        else:
            going_west.append(i)

    total_west = len(going_west)
    total_east = len(going_east)
    last_west = 0
    last_total = 0
    count = 0

    for i in range(total_east):
        if count > 1000000000:
            return -1

        for j in range(last_west, total_west + 1):
            if j == total_west:
                last_west = total_west
                count += last_total
            elif going_east[total_east - i - 1] < going_west[total_west - j - 1]:
                last_total += 1
            else:
                count += last_total
                last_west = j
                break

    if count > 1000000000:
        return -1

    return count



def decent_solution(A): # Gives 100% on codility, but very verbose for what this should be...
    going_east = []
    going_west = []

    count = 0

    for i in range(len(A)):
        if A[i] == 0:
            going_east.append(i)
        else:
            going_west.append(i)

    last_west = len(going_west) - 1
    last_total = 0

    for i in range(len(going_east) - 1, -1, -1):
        if last_west == -100:
            count += last_total
            continue
        for j in range(last_west, -2, -1):
            if count > 1000000000:
                return -1
            if j == -1:
                count += last_total
                last_west = -100
            elif going_east[i] < going_west[j]:
                last_total += 1
            else:
                count += last_total
                last_west = j
                break

    if count > 1000000000:
        return -1

    return count


def first_solution(A):  # O(n^2)?
    going_east = []
    going_west = []

    count = 0

    for i in range(len(A)):
        if A[i] == 0:
            going_east.append(i)
        else:
            going_west.append(i)

    for east in going_east:
        for west in going_west:
            if west > east:
                count += 1

    if count > 1000000000:
        return -1

    return count


if __name__ == '__main__':
    print(solution([0, 1, 0, 1, 1]))
    print(solution([1]))
    print(solution([0]))
    print(solution([1,0,1,1,1,0,1,1,1,0,0,1]))
    print(solution([0,0,1]))
    print(solution([1,0,1,0,1,0,0,1]))