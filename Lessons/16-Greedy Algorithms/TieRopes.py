def solution(K, A): # O(N), 100%
    rope_count = 0
    last_rope = 0

    for i in A:
        if i + last_rope < K:
            last_rope = i + last_rope
        else:
            last_rope = 0
            rope_count += 1

    return rope_count


if __name__ == '__main__':
    print(solution(4, [1, 2, 3, 4, 1, 1, 3]))
    print(solution(1, [1,2,3,4,1,1,3]))



#[1 + 2 + 3, 4, 1 + 1 + 3]