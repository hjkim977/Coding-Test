a=[list(map(int, input().split())) for _ in range(9)]
max_value=0
r=0
c=0
for i in range(9):
    for j in range(9):
        if a[i][j]>=max_value:
            max_value=a[i][j]
            r=i+1
            c=j+1
print(max_value)
print(r,c)