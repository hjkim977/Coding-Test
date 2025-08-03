import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # n : 심사대, m : 사람
time = [int(input()) for _ in range(n)]
result = float('inf')

left = 1
right = max(time)*m

while left<=right:
    mid = (left+right)//2 # mid시간동안 몇명을 처리할 수 있는지
    total = 0 # mid시간동안 처리할 수 있는 사람 수
    
    for t in time:
        total += mid//t
    
    if total>=m:
        right = mid-1
        result = min(result,mid)
    else:
        left = mid+1
print(result)