from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖으로 나가면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽이거나 이미 방문한 경우
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우에만 거리 갱신
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

# 결과 출력
print(bfs(0, 0))