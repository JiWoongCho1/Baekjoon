list_ = sorted(list(map(int, input().split())))
a, b, c = list_[0], list_[1], list_[2]

if c < a + b:

    answer = a + b + c
else:
    c = a + b - 1
    answer = a + b + c
print(answer)