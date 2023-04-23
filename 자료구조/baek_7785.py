n = int(input())
dic_ = {}
name_list = []
for i in range(n):
    name, inout = input().split()

    if inout == 'enter':
        dic_[name] = 1
    else:
        del dic_[name]

dic_ = sorted(dic_.keys(), reverse =True )
for i in dic_:
    print(i)
