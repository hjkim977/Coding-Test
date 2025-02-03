n,m = map(int,input().split())
a=[[0 for j in range(m)]for i in range(n)]
b=[[0 for j in range(m)]for i in range(n)]
arr=[[0 for j in range(m)]for i in range(n)]

for i in range(n):
    a[i]=list(map(int,input().split()))
for i in range(n):
    b[i]=list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        arr[i][j]=a[i][j]+b[i][j]

for row in arr:
    print(*row)