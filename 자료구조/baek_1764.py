n, m = map(int, input().split())
dic_n = {}

cnt_list = []
for _ in range(n):
    dic_n[input()] = 1

for _ in range(m):
    name = input()
    if name in dic_n.keys():

        cnt_list.append(name)
print(len(cnt_list))
for word in sorted(cnt_list):
    print(word)
