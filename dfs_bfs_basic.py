# 문제 : boj.kr/1206
# dfs, bfs 기본문제.
import sys
from collections import deque
def dfs(v): #깊이우선탐색
    print(v, end = ' ')
    visited[v] = 1 # 방문처리
    for i in range(1, n+1): #연결된 노드 중에 방문하지 않은 노드 방문해 재귀함수 돌리기
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
def bfs(v): #너비우선탐색
    queue = [v] #큐 스택에 하나씩 넣어준다.
    visited[v] = 0 # dps 함수 돌린 상태라 방문한 노드는 1이므로 0으로 바꿔준다.
    while queue:
        v = queue.pop(0) #데크를 따로 사용하지 않고 선입선출을 해준다.
        print(v, end = ' ')
        for i in range(1, n+1):
            if visited[i] == 1 and graph[v][i] ==1:
                queue.append(i)
                visited[i] = 0

input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
bfs(v)


