# 백준 11724

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # recursion 오류

def dfs(graph, v, visited):
      visited[v] = True
      for i in graph[v]:
            if visited[i] == False:
                  dfs(graph, i, visited)

n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [[]for i in range(n+1)]

for i in range(m):
      u, v = map(int, input().split())
      # 양방향으로 추가해야 하는것 잊지 말것!
      graph[u].append(v)
      graph[v].append(u)

count = 0

for i in range(1,n+1):
      if visited[i] == False:
            dfs(graph, i, visited)
            count+=1

print(count)