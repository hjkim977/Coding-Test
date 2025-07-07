from collections import deque
def solution(maps):
    i = len(maps) #행
    j = len(maps[0]) #열
    
    visited = [[False]*j for _ in range(i)]
    result = []
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        visited[x][y] = True
        total = int(maps[x][y])
        
        while q:
            x,y = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<i and 0<=ny<j and not visited[nx][ny] and maps[nx][ny]!='X':
                    visited[nx][ny] = True
                    total += int(maps[nx][ny])
                    q.append((nx,ny))
        return total

    for a in range(i):
        for b in range(j):
            if not visited[a][b] and maps[a][b] != 'X':
                result.append(bfs(a, b))
    if result:
        result.sort()
        return result
    else:
        return [-1]