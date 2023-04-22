n_list = []
for _ in range(5):
    n_list.append(int(input()))
n_list = sorted(n_list)

median = n_list[2]
mean = int(sum(n_list)/5)
print(mean)
print(median)
