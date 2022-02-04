#문제 : https://www.acmicpc.net/problem/2089
#진수법을 이용. 어려우니 다시 봐야할 듯.
import sys
input = sys.stdin.readline

n = int(input())

if not n:
    print("0")
    exit()
res = ''
while n:
    if n % (-2): #나머지가 0이 아니라면
        res = '1' + res
        n = n //-2 + 1
    else:
        res = '0' + res
        n //= -2
print(res)
