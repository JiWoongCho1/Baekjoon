n = int(input())
tree_list = []
gap_list = []


def gcd(x, y): # x < y
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y

for _ in range(n):
    tree_list.append(int(input()))

for i in range(1, len(tree_list)):
    gap_list.append(tree_list[i] - tree_list[i-1])

gap_set = list(set(gap_list))
gcd_ = gap_set[0]

for i in range(1, len(gap_set)):
    gcd_ = gcd(gap_set[i], gcd_)


cnt = 0
for i in gap_list:
    cnt += i // gcd_ - 1
print(cnt)