n = int(input())

n_list = list(map(int, input().split()))

origin_list = sorted(list(set(n_list)))

dic = {origin_list[i] : i for i in range(len(origin_list))}

for i in n_list:
    print(dic[i], end = ' ')

