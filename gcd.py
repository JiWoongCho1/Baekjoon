#문제 : https://www.acmicpc.net/problem/9613
#gcd 함수, 조합함수 이용해서 합 구함
from itertools import combinations
import math
t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    answer = 0
    del n[0]
    ncr = combinations(n, 2)
    for j,k in ncr:
        answer += math.gcd(j,k)
    print(answer)
