
a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(x, y): # x < y
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y

g1 = gcd(b, d)
demon = b * d // g1
mole = a * (d // g1) + c * (b // g1)

g2 = gcd(demon, mole)
print(mole // g2, demon // g2)






