## 시간초과 코드

n, m = map(int, input().split())
dic_ = {}


for i in range(1, n+1):
    t = input()
    dic_[t] = i
    dic_[i] = t

for j in range(m):
    q = input()
    if q.isdigit() is True:
        print(dic_[int(q)])
    else:
        print(dic_[q])

## 정답코드
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
