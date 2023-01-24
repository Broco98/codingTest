# 백준 1920

# in 구문을 사용하면 시간이 초과됨 -> 이진탐색으로 구현
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort() # 이진탐색은 정렬된 리스트에서만 사용 가능

for i in range(m):
    
    target = m_list[i]
    head = 0
    tail = n-1
    mid = (head + tail) // 2
    
    while head <= tail:
        if n_list[mid] == target:
            print(1)
            break
        elif n_list[mid] > target:
            tail = mid-1
        else:
            head = mid+1
        mid = (head+tail)//2
    
    if not n_list[mid] == target:
        print(0)