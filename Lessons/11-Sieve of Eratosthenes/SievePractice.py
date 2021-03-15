# Returns all prime numbers between 0 and n
def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    i = 2
    while i*i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1

    nums = []
    for i in range(len(sieve)):
        if sieve[i]:
            nums.append(i)

    return nums

if __name__ == '__main__':
    print(sieve(100))