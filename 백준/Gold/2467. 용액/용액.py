import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int,input().split()))
liquid.sort()

left = 0
right = n-1
result = [0,0]
min_total = float('inf')

while left<right:
    total = liquid[left]+liquid[right]

    if abs(total)<min_total:
        min_total = abs(total)
        result = [liquid[left],liquid[right]]

    if total<0:
        left+=1
    else:
        right-=1
        
print(result[0],result[1])