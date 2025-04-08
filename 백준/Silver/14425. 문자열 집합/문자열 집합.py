n,m=map(int, input().split())
s=[input() for _ in range(n)] #s에 포함되어 있는 문자열
w=[input() for _ in range(m)] #검사해야 하는 문자열
c=0

for i in w:
    if i in s:
        c+=1
print(c)