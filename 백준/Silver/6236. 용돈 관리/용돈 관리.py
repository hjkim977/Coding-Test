n,m = map(int,input().split())
use = list(int(input()) for _ in range(n))

min_money = float('inf')
left = max(use)
right = sum(use)

def manage(left,right):
    global min_money

    while left<=right:
        mid = (left+right)//2
        cnt = 1
        total = 0

        for i in use:
            if total+i>mid:
                cnt+=1
                total = i
            else:
                total+=i
        if cnt<=m:
            min_money = min(min_money,mid)
            right = mid-1
        else:
            left = mid+1
        
manage(left,right)
print(min_money)