from collections import deque
n=int(input())
trees=[[] for _ in range(n+1)]
visited=[False]*(n+1) #방문처리 여부
parent=[0]*(n+1) #부모 정보 저장장

for _ in range(n-1):
    a,b=list(map(int,input().split()))
    trees[a].append(b)
    trees[b].append(a)

def bfs(start):
    queue=deque([start])
    visited[start]=True

    while queue:
        node=queue.popleft()
        for neighbor in trees[node]:
            if not visited[neighbor]:
                parent[neighbor]=node #부모 저장
                visited[neighbor]=True
                queue.append(neighbor)

bfs(1)
for i in range(2,n+1):
    print(parent[i])