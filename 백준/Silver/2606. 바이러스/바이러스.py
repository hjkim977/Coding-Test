n=int(input())
m=int(input())
networks=[[] for i in range(n+1)] 

for _ in range(m):
    a,b=list(map(int,input().split()))
    networks[a].append(b)
    networks[b].append(a)

visited=[0]*(n+1)
def dfs(v):
    visited[v]=1
    for network in networks[v]:
        if visited[network]==0:
            dfs(network)

dfs(1)
print(visited.count(1)-1)