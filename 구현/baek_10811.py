n, m = map(int, input().split())

pocket = [i for i in range(0, n+1)]


for _ in range(m):
    i, j = map(int, input().split())
    r = j - i + 1
    for k in range(r // 2):
        temp = pocket[i]
        pocket[i] = pocket[j]
        pocket[j] = temp
        i += 1
        j -= 1
for i in pocket[1:]:
    print(i, end = ' ')
