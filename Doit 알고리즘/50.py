# 백준 1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(a, arr_check):
    if arr_check[a] == a:
        return a
    else:
        arr_check[a] = find(arr_check[a], arr_check) # 핵심! find -> 경로 압축
        return arr_check[a]

def union(a, b, arr_check):
    find_a = find(a, arr_check)
    find_b = find(b, arr_check)
    
    if find_a != find_b:
        arr_check[find_b] = find_a # 대표 하나만 바꿔도 연결된 나머지는 find하면서 자동으로 바꿈
    
def checkSame(a, b, arr_check):
    find_a = find(a, arr_check)
    find_b = find(b, arr_check)
    if find_a == find_b:
        return True
    else:
        return False

n, m = map(int, input().split())
arr_check = [x for x in range(n+1)]

for i in range(m):
    c, u, v = map(int, input().split())
    if c == 0:
        union(u, v, arr_check)
    else:
        if checkSame(u, v, arr_check):
            print("YES")
        else:
            print("NO")

