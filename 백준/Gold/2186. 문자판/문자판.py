import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
arr = [input().strip() for _ in range(n)]
word = input().strip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

l = len(word)
dp = [[[-1]*l for _ in range(m)] for _ in range(n)]
# dp[x][y][idx]
# -1을 넣었다는 건 아직 경로를 계산하지 않았다는 말

def dfs(x,y,idx): # idx:몇번째 글자를 찾는 중인지
    if idx == l-1: # 글자가 완성되면 카운트 추가
        return 1
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    total = 0
    
    for move in range(1,k+1): # 1~k칸까지 이동 가능하기 떄문
        for i in range(4):
            nx,ny = x+dx[i]*move, y+dy[i]*move
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==word[idx+1]:
                    total += dfs(nx,ny,idx+1)
    dp[x][y][idx] = total
    return total

for a in range(n):
    for b in range(m):
        if arr[a][b]==word[0]:
            cnt += dfs(a,b,0)

print(cnt)