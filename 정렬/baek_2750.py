n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))
n_list = sorted(n_list)

for j in n_list:
    print(j)