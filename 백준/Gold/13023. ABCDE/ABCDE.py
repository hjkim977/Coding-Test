import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*n
def dfs(node,cnt):
    if cnt==4:
        print(1)
        sys.exit()

    visited[node] = 1    
    for nn in graph[node]:
        if not visited[nn]:
            dfs(nn,cnt+1)
    visited[node]=0
for i in range(n):
    dfs(i,0)
print(0)