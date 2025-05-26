from collections import deque
n,m = map(int,input().split()) #n:행, m:열

graph = [list(map(int,input().split())) for i in range(n)]
distance=[[-1]*m for _ in range(n)] #출력
visited=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#목표 지점 찾기(2찾기)
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            a,b=i,j

def bfs(a,b):
    q=deque([[a,b]])
    visited[a][b]=True
    distance[a][b]=0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]!=0:
                q.append([nx,ny])
                visited[nx][ny]=True
                distance[nx][ny]=distance[x][y]+1

bfs(a,b)

#출력
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print() #줄바꿈