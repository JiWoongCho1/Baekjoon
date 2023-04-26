n = int(input())


def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


for _ in range(n):
    z = int(input())
    while True:
        if isPrime(z):
            print(z)
            break
        else:
            z += 1

