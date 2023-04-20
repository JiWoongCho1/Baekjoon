n, m = map(int, input().split())

numbers = sorted(list(map(int, input().split())))
answer_list = []

for i in range(n):
    first = numbers[i]
    for j in range(i+1, n):
        second = numbers[j]
        for k in range(j+1, n):
            third = numbers[k]
            answer = first + second + third
            if answer <= m:

                answer_list.append(answer)

print(max(answer_list))