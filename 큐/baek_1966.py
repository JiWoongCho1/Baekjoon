from collections import deque
t = int(input())

for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    queue = deque(list(input().split()))

    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) -1



