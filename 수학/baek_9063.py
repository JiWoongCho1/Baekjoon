n = int(input())
height = []
width = []
for i in range(n):
    h, w = map(int, input().split())
    height.append(h)
    width.append(w)
answer = (max(height) -min(height)) * (max(width)-min(width))
print(answer)
