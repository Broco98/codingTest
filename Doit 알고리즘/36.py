# 백준 1541

n = list(input().split('-'))
result = 0

for i in range(len(n)):
    sum = 0
    for j in n[i].split('+'):
        sum += int(j)
        
    if i == 0:
        result += sum
    else:
        result -= sum
    
print(result)