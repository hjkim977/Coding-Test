import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
g = list(map(int,input().split()))

left = max(g)
right = sum(g)

def bluray(mid):
    cnt = 1
    total = 0
    for i in g:
        if total+i > mid:
            cnt += 1
            total = i
        else:
            total += i
    return cnt

result = 0
while left <= right:
    mid = (left+right)//2
    cnt = bluray(mid)

    if cnt<=m:
        result = mid
        right = mid-1
    else:
        left = mid+1
print(result)