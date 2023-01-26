# 백준 1753

import sys
from queue import PriorityQueue # 우선순위 큐
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
INF = 987654321
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

que = PriorityQueue()
que.put((0,k))
result = [INF] * (n+1)
result[k] = 0
visited = [False] * (n+1)

while que.qsize()>0: # 그냥 que 사용하면 안됨
    current = que.get()
    current_node = current[1]
    if visited[current_node]:
        continue
    visited[current_node] = True
    for i in graph[current_node]:
        next = i[0]
        weight = i[1]
        if result[next] > result[current_node] + weight:
            result[next] = result[current_node] + weight
        que.put((result[next], next))
            
for i in range(1, n+1):
    if visited[i]:
        print(result[i])    
    else:
        print("INF")