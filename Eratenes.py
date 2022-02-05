#문제 : https://www.acmicpc.net/problem/1929
#에레토스테네스의 체 : 다수 소수 판별식
#그 수를 소수 판별하는 것이 아니라 수의 제곱근까지 판별해도 됨.
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m,n+1):
    if isPrime(i):
        print(i)
