n = int(input())

for i in range(n):
    ans = []
    a,b = map(int, input().split())
    A, B = a,b
    while a != 0:
        b = b % a #새롭게 할당된 b < a 이유: 나머지가 나누는 값보다 클 수 없음
        a, b = b, a  #
    gcd = b
    lcm = A * B // gcd
    print(lcm)

#푼 방식 : 유클리드 호제법