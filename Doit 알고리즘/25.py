# 백준 1260

import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    
def bfs(graph, v, visited):
    que = deque()
    que.append(v)
    while que:
        now = que.popleft()
        print(now, end = ' ')
        visited[now] = True
        for i in graph[now]:
            if visited[i] == False and (i not in que):
                que.append(i)
    return 0

n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
for i in range(1,n+1):
    graph[i].sort()
    
dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)