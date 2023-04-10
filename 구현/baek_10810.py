n, m = map(int, input().split())

basket = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for s in range(i, j+1):
        basket[s] = k

for i in basket[1:]:
    print(i, end = ' ')