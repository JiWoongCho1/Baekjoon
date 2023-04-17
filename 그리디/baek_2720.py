number = int(input())

q = 25
d = 10
n = 5
p = 1

for _ in range(number):
    pay_list = []
    pay = int(input())

    quarter = pay // q
    pay -= quarter * q
    pay_list.append(quarter)

    dime = pay // d
    pay -= dime * d
    pay_list.append(dime)

    nikel = pay // n
    pay -= nikel * n
    pay_list.append(nikel)

    penny = pay // p
    pay -= penny * p
    pay_list.append(penny)

    print(*pay_list)
