#문제 : boj.kr/11724
#dfs 문제
import sys
sys.setrecursionlimit(10000)
count = 0
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    for k in range(1,n+1):
        if graph[v][k] == 1 and visited[k] == 0:
            dfs(k)

for _ in range(m):
    v, u = map(int, input().split())
    graph[v][u] = 1
    graph[u][v] = 1

for i in range(1, len(visited)):
    if visited[i] == 0:
        count += 1
        dfs(i)

print(count)