#문제 : https://www.acmicpc.net/problem/2004
#주의할 점: factorial 쓰면은 시간초과 남.


input = sys.stdin.readline

n, m = map(int, input().split())
def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

five_count = count_number(n,5) - count_number(m,5) -count_number(n-m, 5)
two_count = count_number(n,2) - count_number(m,2) -count_number(n-m, 2)
print(min(five_count, two_count))
