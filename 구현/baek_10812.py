n, m =  map(int, input().split())

pocket = [i for i in range(1, n+1)]

for _ in range(m):
    begin, end, mid = map(int, input().split())

    pocket = pocket[:begin-1]+ pocket[mid-1:end] + pocket[begin-1:mid-1] + pocket[end:]
for i in pocket:
    print(i, end = ' ')

