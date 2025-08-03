from collections import deque

def bfs(si,sj,v):
    q= deque()

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=1

def solve():
    global arr, n, m
    for year in range(1, 900000): # 왜 90만까지? 300*300=90,000번 이상 반복할 일을 사실 없지만 안전하게 여유를 둬서 큰 수 씀
        # 1. 둘러싼 0의 개수 카운트
        a_sub = [[0]*m for _ in range(n)]
        for i in range(1,n-1): # 가장자리는 0으로만 채워져 있으니까 n-1, m-1이 됨
            for j in range(1,m-1):
                if arr[i][j]==0:
                    continue
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if arr[ni][nj]==0:
                        a_sub[i][j]+=1

        # 2. 높이 낮추기
        for i in range(1,n-1):
            for j in range(1,m-1):
                if a_sub[i][j]>0:
                    arr[i][j]=max(0,arr[i][j]-a_sub[i][j])

        # 3. 덩어리 개수 카운트 (bfs)
        v = [[0]*m for _ in range(n)] # 방문배열
        cnt = 0

        for i in range(1,n-1):
            for j in range(1,m-1):
                if v[i][j]==0 and arr[i][j]>0:
                    bfs(i,j,v)
                    cnt+=1
                    if cnt>1: # 두 덩어리 이상
                        return year
        if cnt==0: #덩어리 개수 0이면 멈추기
            return 0

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = solve()
print(ans)