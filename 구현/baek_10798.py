row =5
matrix = []
answer = []

for i in range(row):
    inputs = list(input())
    new_list = []
    for k in inputs:

        new_list.append(k)
    matrix.append(new_list)

    if len(matrix[i]) != 15:
        for j in range(15 - len(matrix[i])):
            matrix[i].append('!')

column = 15

for i in range(column):
    for j in range(row):
        answer.append(matrix[j][i])

for word in answer:
    if word == '!':
        pass
    else:
        print(word, end ='')