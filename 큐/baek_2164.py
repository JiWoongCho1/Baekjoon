from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])


while len(queue) > 1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)

print(queue[0])

