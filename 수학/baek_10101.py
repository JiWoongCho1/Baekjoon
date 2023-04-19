a_list = []
for i in range(3):
    a = int(input())
    a_list.append(a)

a, b, c = a_list[0], a_list[1], a_list[2]

while True:
    if a == b and b == c:
        print('Equilateral')
        break

    if a + b + c == 180:
        if a == b or b == c or c == a:
            print('Isosceles')
            break
        else:
            print('Scalene')
            break
    else:
        print('Error')
        break
