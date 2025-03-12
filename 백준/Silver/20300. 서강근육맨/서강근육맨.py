n=int(input())
t=list(map(int,input().split()))
t.sort()
m=0 #크기를 비교할 비교군이 있어야함

if n%2==0: # 2 5 8 13 23 25
    for i in range(n//2):
        m=max(m, t[i]+t[-(i+1)])
else: #2 5 8 13 23 25 26
    for i in range(n//2):
        m=max(m, t[i]+t[-(i+2)])
    m=max(m,t[-1])

print(m)