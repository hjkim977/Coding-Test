n = int(input())
mp, mf, ms, mv = list(map(int,input().split()))
a= [list(map(int,input().split())) for _ in range(n)]

price = float('inf')
result = []

def diet(idx,p,f,s,v,money,picked):
    global price, result

    if idx==n:
        if p>=mp and f>=mf and s>=ms and v>=mv:
            if price > money:
                price = money
                result = picked
            elif price == money:
                if result > picked:
                    result = picked
        return
        
    # 1. 현재 재료 선택 안함
    diet(idx+1,p,f,s,v,money,picked)

    # 2. 현재 재료 선택
    np,nf,ns,nv,nm= a[idx]
    diet(idx+1,p+np,f+nf,s+ns,v+nv,money+nm,picked+[idx+1])

diet(0,0,0,0,0,0,[])

if price == float('inf'):
    print(-1)
else:
    print(price)
    print(*result)