def binary_search(A, x, l, r):
    if r < l:
        return -1

    mid = l + (r - l) // 2

    if A[mid] == x:
        return mid
    elif A[mid] > x:
        return binary_search(A, x, l, mid - 1)
    else:
        return binary_search(A, x, mid + 1, r)


if __name__ == '__main__':
    A = [1,3,5,6,7]
    print(binary_search(A, 1, 0, len(A) - 1))
    print(binary_search(A, 3, 0, len(A) - 1))
    print(binary_search(A, 5, 0, len(A) - 1))
    print(binary_search(A, 6, 0, len(A) - 1))
    print(binary_search(A, 7, 0, len(A) - 1))
    print(binary_search(A, 8, 0, len(A) - 1))
