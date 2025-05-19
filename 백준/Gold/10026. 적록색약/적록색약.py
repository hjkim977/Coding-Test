#bfs
from collections import deque
n = int(input())
f = [list(input().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color,visited,f):
    q=deque()
    q.append((x,y))
    visited[x][y]=1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and f[nx][ny]==color:
                visited[nx][ny]=1
                q.append((nx,ny))

#적록색약 아닌 사람
a=0
visited=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,f[i][j],visited,f)
            a+=1

#적록색약
b=0
visited=[[0]*n for _ in range(n)]
# 적록색약을 위한 배열 복사 및 색상 변경
copy_f = []
for i in range(n):
    row = []
    for j in range(n):
        if f[i][j] == 'G':
            row.append('R')  # G는 R로 바꿈
        else:
            row.append(f[i][j])  # 나머지는 그대로
    copy_f.append(row)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,copy_f[i][j],visited,copy_f)
            b+=1

print(a, b)