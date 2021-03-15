def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fibonacci_dynamic(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

def matrix_2x2_multiply(A,B):
    top_left = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    top_right = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    bottom_left = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    bottom_right = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    return [[top_left, top_right], [bottom_left, bottom_right]]

def matrix_fibonacci(n):
    initial_matrix = [[1, 1],[1, 0]]
    result_matrix = [[1, 0],[0, 1]] # Identity matrix

    for i in range(n):
        result_matrix = matrix_2x2_multiply(result_matrix, initial_matrix)

    return result_matrix[0][1]

if __name__ == '__main__':
    for i in range(12):
        print(fib(i))
    print("DYNAMIC FIB")
    for i in range(12):
        print(fibonacci_dynamic(i))
    print("MATRIX FIB")
    for i in range(12):
        print(matrix_fibonacci(i))