#bfs
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
donut = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = (x+dx[i])%n,(y+dy[i])%m
            if not visited[nx][ny] and donut[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny))
cnt=0
for i in range(n):
    for j in range(m):
        if donut[i][j]==0 and not visited[i][j]:
            bfs(i,j)
            cnt+=1
print(cnt)