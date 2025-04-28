import sys
input=sys.stdin.readline
n,m=list(map(int,input().split()))
count=0

con=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=list(map(int,input().split()))
    con[u].append(v)
    con[v].append(u)

visited=[0]*(n+1)

def dfs(a):
    stack=[a]
    while stack:
        node=stack.pop()
        if not visited[node]:
            visited[node]=1
            for i in con[node]:
                if not visited[i]:
                    stack.append(i)

for a in range(1,n+1):
    if visited[a]==0:
        dfs(a)
        count+=1

print(count)