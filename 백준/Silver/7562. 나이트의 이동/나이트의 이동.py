import sys
from collections import deque
input=sys.stdin.readline

moves=[(-2,-1),(-1,-2),(1,-2),(2,-1),
       (2,1),(1,2),(-1,2),(-2,1)]

def bfs(l,start,end):
    visited=[[0]*l for _ in range(l)]
    queue=deque()
    queue.append((start[0],start[1],0))
    visited[start[0]][start[1]] = 1

    while queue:
        x,y,count=queue.popleft()
        if (x,y)==end:
            return count
        
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny,count+1))

test=int(input())
for _ in range(test):
    l=int(input())
    start=tuple(map(int,input().split()))
    end=tuple(map(int,input().split()))
    print(bfs(l,start,end))