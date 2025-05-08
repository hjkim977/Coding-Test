import sys
sys.setrecursionlimit(10**6)

n=int(input())
area=[list(map(int,input().split())) for _ in range(n) ]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,h,visited):
    visited[x][y]=True
    for i in range(4):
        nx,ny= x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and area[nx][ny]>h:
            dfs(nx,ny,h,visited)

max_area=0

#비 안오는 경우부터 최대 높이까지 반복
for h in range(0,max(map(max,area))+1):
    visited=[[False]*n for _ in range(n)]
    cnt=0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j]>h:
                dfs(i,j,h,visited)
                cnt+=1
    max_area = max(max_area, cnt)

print(max_area)