from collections import deque

m,n = map(int,input().split()) #m=열, n=행
box=[list(map(int,input().split())) for _ in range(n)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    for i in range(n):
        for j in range(m):
            if box[i][j]==1:
                q.append((i,j))
    while q:            
        x,y=q.popleft()
        for a in range(4):
            nx, ny = x+dx[a], y+dy[a]
            if 0<=nx<n and 0<=ny<m and box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                q.append((nx,ny))
            
bfs()

day=0
for row in box:
    if 0 in row: #row에 하나라도 0이 있다면
        print(-1)
        exit() #-1을 출력하고 그 다음부터는 확인할 필요 없으니까 바로 탈출
    day=max(day,max(row))
print(day-1) 