# 백준 11659번

# 이거 없으면 시간 초과뜸 ㅋㅋ
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