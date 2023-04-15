row = 9
column = 9

row_list = []
max_row = 1
max_column = 1
max_number = 0
for i in range(row):
    numbers = list(map(float, input().split()))
    row_list.append(numbers)

for i in range(1, row+1):
    for j in range(1, column+1):
        number = row_list[i-1][j-1]
        if number >= max_number:
            max_number = number
            max_row = i
            max_column = j
print(int(max_number))
print()
print(max_row, max_column)