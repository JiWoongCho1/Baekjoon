n, m = map(int, input().split())

basket = [i for i in range(0, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    basket[j], basket[i] = basket[i], basket[j]

for i in basket[1:]:
    print(i, end = ' ')