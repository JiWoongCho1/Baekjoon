
n = int(input())


def gcd(m, n):

    if m < n:
        while m != 0:
            n = n % m
            m, n = n, m
        return n
    else:
        while n != 0:
            m = m % n
            n, m = m, n
        return m


for _ in range(n):
    nums = list(map(int, input().split()))
    n = nums[0]
    sum = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            sum += gcd(nums[i], nums[j])
    print(sum)

## 런타임에러나온 코드


