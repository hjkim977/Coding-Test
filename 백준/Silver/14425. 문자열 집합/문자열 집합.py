n,m=map(int, input().split())
s={input() for _ in range(n)}
c=0

for _ in range(m):
    i=input()
    if i in s:
        c+=1
print(c)