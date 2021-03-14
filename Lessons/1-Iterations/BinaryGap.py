def solution(N):
    binary_string = bin(N)[2:]
    binary_length = len(binary_string)

    longest_seq = 0
    left_idx = 0
    while left_idx < binary_length:
        if binary_string[left_idx] == '1':
            current_seq = 0
            for j in range(left_idx + 1, binary_length):
                if j == binary_length - 1:
                    left_idx = j - 1
                if binary_string[j] == '0':
                    current_seq += 1
                else:
                    left_idx = j - 1
                    break
            left_idx += 1
            if left_idx == binary_length - 1:
                if binary_string[left_idx] == '1':
                    longest_seq = max(longest_seq, current_seq)
            else:
                longest_seq = max(longest_seq, current_seq)
        else:
            left_idx += 1

    return longest_seq


if __name__ == '__main__':
    print(solution(0))
    print(solution(9))
    print(solution(529))
    print(solution(20))
    print(solution(15))
    print(solution(32))
    print(solution(1041))
    print(solution(32))
