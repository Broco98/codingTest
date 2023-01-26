# 백준 1516
# 그래프의 노드 순서 -> 위상정렬문제

from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1) # 진입 차수, 들어오는 노드 개수(인바운딩)
time = [0] * (n+1)
result = [0] * (n+1)

for i in range(1,n+1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    index = 1
    while arr[index] != -1:
        node = arr[index]
        graph[node].append(i)
        indegree[i] += 1
        index+=1
        
que = deque()

# 바로 지을 수 있는 건물부터 짓기 시작
for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)
        
while que:
    now = que.popleft()
    for next in graph[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + time[now]) # 이전 건물 짓는 시간을 더하는 것
        if indegree[next] == 0: # 0이라는 의미는 만들 수 있다는 의미 (이전 건물 완성)
            que.append(next)

for i in range(1, n+1):
    print(result[i] + time[i]) # 자기 건물 짓는 시간까지 더해서 출력