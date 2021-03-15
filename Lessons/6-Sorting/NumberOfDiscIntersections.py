#Come back to this problem soon...

def solution(A): # O(n^2) solution, 50% https://app.codility.com/demo/results/training4SCF7N-G8C/
    borders = []

    for i in range(len(A)):
        start = i - A[i]
        end = i + A[i]
        borders.append((start, end))

    count = 0
    n = len(A)

    visited = set()

    for i in range(len(borders)):
        left1, right1 = borders[i]

        if count > 10000000:
            return -1

        for j in range(len(borders)):
            if (j, i) in visited or i == j:
                continue
            left2, right2 = borders[j]
            if (right1 >= left2 >= left1) or (left1 <= right2 <= right1) or (left1 <= left2 and right1 >= right2):
                visited.add((i,j))
                count += 1
    return count


if __name__ == '__main__':
    print(solution([1,5,2,1,4,0]))