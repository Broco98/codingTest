# 백준 1929

# 시간초과
# 핵심은 sqrt(n)까지 탐색해도 된다는 것임 -> n = a*b에서, a,b모두 n을 넘을 수 없기 때문

import math

m, n = map(int, input().split())

arr = [x for x in range(n+1)] # 헷갈리지 않게 0 ~ n까지 생성

for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == 1:
        continue
    for j in range(i+i, n+1, i): # i자신을 제외한 i의 배수 지워주기
        arr[j] = 1

for i in range(m, n+1):
    if arr[i] != 1:
        print(arr[i])