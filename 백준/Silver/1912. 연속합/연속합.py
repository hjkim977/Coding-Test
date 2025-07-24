n = int(input())
l = list(map(int,input().split()))
d = [0]*n
d[0] = l[0]

for i in range(1,n):
    d[i] = max(l[i],d[i-1]+l[i])

print(max(d))