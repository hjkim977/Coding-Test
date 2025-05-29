from collections import deque
import sys
input=sys.stdin.readline

m,n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
sx,sy,sd = map(int, input().split())
ex,ey,ed = map(int, input().split())
visited = [[[False]*4 for _ in range(n)] for _ in range(m)]

# 좌표 맞추기
sx -= 1
sy -= 1
sd -= 1
ex -= 1
ey -= 1
ed -= 1

dx=[0, 0, 1, -1] #동서남북
dy=[1, -1, 0, 0]

# 회전 함수, d는 현재방향
def turn_left(d):
    return [3, 2, 0, 1][d]

def turn_right(d):
    return [2, 3, 1, 0][d]

q = deque()
q.append((sx, sy, sd, 0))
visited[sx][sy][sd] = True

def bfs():
    while q:
        x, y, d, cnt = q.popleft()

        if x == ex and y == ey and d == ed:
            print(cnt)
            break

        # 앞으로 1~3칸 가기
        for k in range(1, 4):
            nx = x + dx[d] * k
            ny = y + dy[d] * k

            if not (0 <= nx < m and 0 <= ny < n): #범위를 벗어나는지
                break
            if grid[nx][ny] == 1: #벽이 있으면 전진 안됨
                break
            if not visited[nx][ny][d]: #방문 안했으면
                visited[nx][ny][d] = True
                q.append((nx, ny, d, cnt + 1)) #명령수 +1해서 추가가

        # 왼쪽 회전
        nd = turn_left(d)
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x, y, nd, cnt + 1))

        # 오른쪽 회전
        nd = turn_right(d)
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x, y, nd, cnt + 1))
bfs()