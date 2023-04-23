n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))
dic_ = {}
for i in range(len(arr1)):
    dic_[arr1[i]] = 0

for i in range(m):
    if arr2[i] not in dic_:
        print(0, end = ' ')
    else:
        print(1, end = ' ')