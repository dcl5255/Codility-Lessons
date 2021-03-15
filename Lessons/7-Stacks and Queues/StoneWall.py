from collections import deque

# Come back to this one later, not sure if I understand the problem entirely

def add_to_blocks(blocks, new_blocks):
    while new_blocks:
        blocks.append(new_blocks.pop())


def block_found(blocks, current):
    removed = deque()

    while blocks:
        last_block = blocks.pop()
        removed.append(last_block)
        if current == last_block:
            add_to_blocks(blocks, removed)
            return True
        if current < last_block:
            continue
        if current > last_block:
            add_to_blocks(blocks, removed)
            return False
    return False


def solution(H):
    blocks = deque()
    count = 0

    for i in H:
        if not block_found(blocks, i):
            blocks.append(i)
            count += 1

    return count


if __name__ == '__main__':
    print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
