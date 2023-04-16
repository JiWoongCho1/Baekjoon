n = int(input())
input_list = [[0 for _ in range(100)] for _ in range(100)]

square_sum = 0

for _ in range(n):
    i, j = map(int, input().split())
    for row in range(i, i+10):

        for col in range(j, j+10):
            input_list[row-1][col-1] = 1


for i in input_list:
    square_sum += i.count(1)
print(square_sum)