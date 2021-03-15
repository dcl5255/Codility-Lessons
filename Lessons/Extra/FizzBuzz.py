def solution():
    for i in range(1,101):
        if i % 3 == 0 or i % 5 == 0:
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            print(s)
        else:
            print(i)


if __name__ == '__main__':
    solution()