# 백준 11003

# deque를 사용하자 -> 시간초과 뜬다
from collections import deque
# import sys
# input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))
D = deque()

for i in range(n):
    while D and D[-1][1] > nums[i]:
        D.pop()
    D.append((i, nums[i]))
    if D[0][0] <= i-l:
        D.popleft()
    print(D[0][1], end=' ')