import sys
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input().strip()) for _ in range(r)]
move = set()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_cnt = 0
move.add(graph[0][0])

def dfs(x,y,cnt):
    global max_cnt
    max_cnt = max(max_cnt,cnt)

    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in move:
            move.add(graph[nx][ny])
            dfs(nx,ny,cnt+1)
            move.remove(graph[nx][ny])

dfs(0,0,1)
print(max_cnt)