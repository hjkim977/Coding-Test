from collections import deque
import sys
input=sys.stdin.readline

r,c=map(int,input().strip().split())
graph=[list(input().strip()) for _ in range(r)]

w_q=deque()
h_q=deque()
visited=[[False]*c for _ in range(r)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':
            w_q.appendleft((x,y))
        elif graph[x][y] == 'S':
            h_q.append((x,y,0))
            
def bfs():
    while h_q:
        #물 먼저
        for _ in range(len(w_q)):
            x,y=w_q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.':
                    graph[nx][ny]='*'
                    w_q.append((nx,ny))
        
        #고슴도치 이동
        for _ in range(len(h_q)):
            x,y,time = h_q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<r and 0<=ny<c:
                    if graph[nx][ny]=='D':
                        print(time+1)
                        exit()
                    if graph[nx][ny]=='.' and not visited[nx][ny]:
                        visited[nx][ny]=True
                        h_q.append((nx,ny,time+1))
    print("KAKTUS")      

bfs()