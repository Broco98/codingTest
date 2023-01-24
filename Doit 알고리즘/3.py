# 백준 11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
sum = 0

for i in arr:
    sum += i
    sum_arr.append(sum)
    
for i in range(m):
    start, end = map(int, input().split())
    print(sum_arr[end] - sum_arr[start-1])