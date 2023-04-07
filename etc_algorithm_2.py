#문제 : https://www.acmicpc.net/problem/1934
n = int(input())

for i in range(n):
    ans = []
    a,b = map(int, input().split())
    A, B = a,b
    while a != 0:
        b = b % a
        a, b = b, a
    gcd = b
    lcm = A * B // gcd
    print(lcm)

#푼 방식 : 유클리드 호제법  github 커밋