import string
lst = string.digits + string.ascii_uppercase # 35진법까지표현가능

def convert(num, base):
    q, r = divmod(num, base)  # 몫과 나머지를 구해주는 함수, 수가 큰수일 때만 효율적
    if q == 0:
        return lst[r]
    else:
        return convert(q, base) + lst[r]
n, b = map(int, input().split())
print(convert(n,b))