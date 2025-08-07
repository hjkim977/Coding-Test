import sys
input = sys.stdin.readline

cnt,e,w,s,n = map(int,input().split())
# 왜 범위가 2*cnt+1?
visited = [[False]*(2*cnt+1) for _ in range(2*cnt+1)]

percent = [e,w,s,n]
dx = [1,-1,0,0] # 동서남북 순으로
dy = [0,0,1,-1]

start = cnt
visited[start][start] = True
answer = 0

def dfs(x,y,move,p):
    global answer

    if move == cnt:
        answer += p #answer에는 단순한 모든 경로의 확률 총합이 저장
        return
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,move+1,p*(percent[i]/100))
            visited[nx][ny] = False # 경로가 끝났으니 칸 방문 여부를 초기화

dfs(start,start,0,1)
print(answer)