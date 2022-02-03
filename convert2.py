# 문제 : https://www.acmicpc.net/problem/2745
import string
n, b = input().split()
n = n[::-1]
b = int(b)

table = string.digits + string.ascii_uppercase
ans = 0

for i in range(len(n)):
    ans += table.index(n[i]) * (b**i)
print(ans)

# 또 다른 간단한 코드, int 함수를 이용 
#int(string , base(꼭 int))
a, b = input().split()
print(int(a, int(b)))