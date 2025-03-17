t=int(input())
for i in range(t):
    n=int(input())
    h=list(map(int,input().split()))
    h.sort()
    
    tree=[0]*n
    left, right=0,n-1  # 좌우 인덱스

    for j in range(n):
        if j%2==0:
            tree[left]=h[j]
            left+=1
        else:
            tree[right]=h[j]
            right-=1
    
    level=0
    for i in range(n):
        level=max(level, abs(tree[i]-tree[i-1]))
    
    print(level)