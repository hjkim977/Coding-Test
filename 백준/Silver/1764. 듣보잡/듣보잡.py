n,m=map(int,input().split())
l={input() for _ in range(n)} #듣도 못한 사람
s={input() for _ in range(m)} #보도 못한 사람

ls=sorted(l&s)
print(len(ls))
for i in ls:
    print(i)