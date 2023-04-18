n, k = map(int, input().split())
answer_list = [0]
for i in range(1, n+1):
    if n % i == 0:
        answer_list.append(i)

if k > len(answer_list)-1:
    print('0')
else:
    print(answer_list[k])
