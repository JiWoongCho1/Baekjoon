while True:
    n = int(input())
    if n == -1:
        break
    answer_list = []
    for i in range(1, n):
        if n % i == 0:
            answer_list.append(i)
    if sum(answer_list) == n:
        print('{} ='.format(n), end=' ')
        for j in answer_list:
            if j != answer_list[-1]:
                print('{} +'.format(j), end = ' ')
            else:
                print('{}'.format(j))

    else:
        print('{} is NOT perfect.'.format(n))

