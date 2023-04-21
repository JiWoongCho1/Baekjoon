n, m = map(int, input().split())
board = list()
answer_list = []

for i in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
                else:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
        answer_list.append(draw1)
        answer_list.append(draw2)
print(min(answer_list))