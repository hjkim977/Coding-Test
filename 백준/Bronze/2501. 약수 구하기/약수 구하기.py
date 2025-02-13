n,k=map(int, input().split())
a=[i for i in range(1,n+1) if n%i==0]

if len(a)<k:
    print(0)
else:
    print(a[k-1])