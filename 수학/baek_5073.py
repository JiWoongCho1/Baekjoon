while True:
    a_list = sorted(list(map(int, input().split())))

    a, b, c = a_list[0], a_list[1], a_list[2]
    if a == 0 or b == 0 or c == 0:
        break

    if c >= a + b:
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or b == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")

