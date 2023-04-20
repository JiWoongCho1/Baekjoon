n = int(input())

answer = 0
generatr = 0


for generator in range(1, n + 1):
    list_ = list(map(int, str(generator)))
    answer = sum(list_) + generator
    if n == answer:
        print(generator)
        break
    elif generator == n:
        print(0)

