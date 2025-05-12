#bfs (횟수의 최솟값)
import sys
input=sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
board=[0]*101 #인덱스가 0부터 시작이니까 101개 만들어줌
visited=[False]*101

ladder={}
for _ in range(n):
    x,y=map(int,input().split())
    ladder[x]=y

snake={}
for _ in range(m):
    u,v=map(int,input().split())
    snake[u]=v

def bfs(start):
    q=deque([start])
    visited[start]=True

    while q:
        current=q.popleft()
        for i in range(1,7):
            next=current+i
            if 0<next<=100 and not visited[next]:
                if next in ladder:
                    next=ladder[next]
                if next in snake:
                    next=snake[next]

                if not visited[next]:
                    q.append(next)
                    visited[next]=True
                    board[next]=board[current]+1

bfs(1)
print(board[100])