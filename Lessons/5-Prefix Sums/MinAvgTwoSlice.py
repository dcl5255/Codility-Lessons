import math

# Works by saving the best average of A in reverse order (starting from the end of A)
def solution(A): # O(N), 100% on codility, https://app.codility.com/demo/results/training55CKRC-26D/

    length = len(A)

    averages = [0] * length
    averages[length - 1] = math.inf
    count = 2

    for i in range(length - 2, -1, -1):
        new_avg = (A[i] + A[i+1])/2
        count += 1
        other_avg = (averages[i+1] * (count - 1) + A[i]) / count
        if new_avg <= other_avg:
            count = 2
            averages[i] = new_avg
        else:
            averages[i] = other_avg

    smallest_index = -1
    smallest_average = math.inf

    for i in range(len(averages)):
        if averages[i] < smallest_average:
            smallest_index = i
            smallest_average = averages[i]

    return smallest_index




def second_solution_modified(A): # O(N) or O(N^2), fully correct. 80% on codility
    smallest_index = -1
    smallest_average = math.inf

    length = len(A)
    for i in range(length - 1):
        if A[i] < smallest_average or i == length - 2:
            current_sum = A[i]
            count = 1
            for j in range(i + 1, length):
                current_sum += A[j]
                count += 1
                if smallest_index == i:
                    if A[j] < smallest_average:
                        current_average = current_sum / count
                        if current_average < smallest_average:
                            smallest_average = current_average
                else:
                    current_average = current_sum / count
                    if current_average < smallest_average:
                        smallest_average = current_average
                        smallest_index = i
    return smallest_index, smallest_average

def second_solution(A): # O(N^2), fully correct, not optimal performance
    smallest_index = -1
    smallest_average = math.inf

    length = len(A)
    for i in range(length - 1):
        current_sum = A[i]
        count = 1
        for j in range(i + 1, length):
            current_sum += A[j]
            count += 1
            if smallest_index == i:
                if A[j] < smallest_average:
                    current_average = current_sum / count
                    if current_average < smallest_average:
                        smallest_average = current_average
            else:
                current_average = current_sum / count
                if current_average < smallest_average:
                    smallest_average = current_average
                    smallest_index = i
    return smallest_index, smallest_average


def sliced(A, P, Q):
    sublist = A[P:Q + 1]
    # print(sublist)
    return sum(sublist) / (Q - P + 1)


def first_solution(A): # O(n^3), fully correct but not very performant
    smallest_index = -1
    smallest_average = math.inf

    length = len(A)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if smallest_index == i:
                if A[j] < smallest_average:
                    current_average = sliced(A, i, j)
                    if current_average < smallest_average:
                        smallest_average = current_average
            else:
                current_average = sliced(A, i, j)
                if current_average < smallest_average:
                    smallest_average = current_average
                    smallest_index = i
    return smallest_index


if __name__ == '__main__':
    print(solution([4,2,2,5,1,5,8]))
    #print(solution([5,6]))
    print(solution([1000,50,-500,0,1,-500,0,-252]))