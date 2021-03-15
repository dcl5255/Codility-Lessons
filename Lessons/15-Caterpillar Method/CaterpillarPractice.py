import time
import random


def caterpillar_method(A, s):  # O(N)
    n = len(A)
    front, total = 0, 0

    for back in range(n):
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        if total == s:
            return True
        total -= A[back]

    return False


def slower_caterpillar(A, s):  # O(NlogN)
    n = len(A)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += A[j]
            if total == s:
                return True
            if total > s:
                break

    return False


def generate_random_array(n, low, high):
    arr = []
    for i in range(n):
        arr.append(random.randint(low, high))
    return arr


if __name__ == '__main__':
    A = generate_random_array(1000, 1, 50)

    for i in range(1000):
        if caterpillar_method(A,i) != slower_caterpillar(A,i):
            print(i)

    start_1 = time.time()
    for i in range(10000):
        caterpillar_method(A, i)
    end_1 = time.time()

    start_2 = time.time()
    for i in range(10000):
        slower_caterpillar(A, i)
    end_2 = time.time()

    print("Caterpillar 1 time: {}".format(end_1 - start_1))
    print("Caterpillar 2 time: {}".format(end_2 - start_2))
