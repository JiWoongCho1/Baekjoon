# 문제 : https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())
stack = [i for i in range(1,n+1)]
answer = []  # 제거된 사람들 넣어줌
num = 0 # 제거 될 사람의 인덱스
for i in range(n):
    num += k-1
    if num >= len(stack):
        num = num % len(stack)
    answer.append(str(stack.pop(num)))
print("<", ", ".join(answer)[:], ">", sep = '')
#변경1
