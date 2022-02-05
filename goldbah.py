#문제 : https://www.acmicpc.net/problem/6588
#에라토스테네스 체 이용
r = 1000000

answer = [False, False] + [True] * (r-1)
    
for i in range(2,1001):
    if answer[i]:
        for j in range(i*2, 1000001, i):
            answer[j] = False

while True:
    n = int(input())
    if n == 0: break
    for i in range(3, len(answer)):
        if answer[i] and answer[n-i]:
            print("{} = {} + {}".format(n,i, n-i))
        