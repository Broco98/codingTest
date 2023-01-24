# 입력받기
n, m = map(int, input().split())
# 그래프 초기화
graph = [[] for _ in range(n + 1)]
# 방문기록 초기화
visited = [False] * (n + 1)

# DFS 알고리즘 -> 재귀 = stack / 재귀도 스택처럼 쌓임
def DFS(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      DFS(i)


for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

count = 0

for i in range(1, n + 1):
  if not visited[i]:
    count += 1
    DFS(i)

print(count)