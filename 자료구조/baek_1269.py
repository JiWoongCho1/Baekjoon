a, b = map(int, input().split())

a_set = set(input().split())
b_set = set(input().split())

cha1 = a_set - b_set
cha2 = b_set - a_set

print(len(cha1)+ len(cha2))