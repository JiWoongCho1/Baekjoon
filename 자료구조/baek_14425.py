n, m = map(int, input().split())
s_list = []
cnt = 0

for _ in range(n):
    s_list.append(input())
for _ in range(m):
    t = input()
    if t in s_list:
        cnt += 1
print(cnt)
