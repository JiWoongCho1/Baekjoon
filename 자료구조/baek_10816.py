n = int(input())
n_list = list(input().split())
m = int(input())
m_list = list(input().split())

dic_ = {}
new_list = list(set(n_list))

for i in range(len(new_list)):
    dic_[new_list[i]] = 1

for i in range(len(n_list)):
    if dic_[n_list[i]]:
        dic_[n_list[i]] += 1

for i in range(m):
    if m_list[i] in dic_.keys():
        if dic_[m_list[i]] > 1:
            print(dic_[m_list[i]] - 1, end = ' ')
        else:
            print(dic_[m_list[i]], end = ' ')
    else:
        print(0, end = ' ')






