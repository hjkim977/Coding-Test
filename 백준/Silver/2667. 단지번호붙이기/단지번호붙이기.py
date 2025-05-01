#dfs
N = int(input())
field = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]  # 방문 여부 체크
result = [] #오름차순으로 출력

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수
def dfs(x, y):
    visited[x][y] = True # 방문 처리를 해주고 단지 크기 증가
    count = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 체크와 방문하지 않았고 집이 있는지 체크
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and not visited[i][j]:  # 집이 있고 아직 방문하지 않았다면
            result.append(dfs(i, j)) #return된 count를 result에 추가

# 단지 번호를 출력하기 위한 정렬
result.sort()

# 결과 출력
print(len(result))  # 단지의 개수
for r in result:  # 각 단지의 크기 출력
    print(r)
