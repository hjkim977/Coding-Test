from itertools import permutations
from collections import deque
n = int(input())
power = list(map(int,input().split()))
attack = [9,3,1]
min_cnt = float('inf')

while len(power)<3:
    power.append(int(0))

visited = [[[False]*61 for _ in range(61)] for _ in range(61)] #최대 체력이 60이니까

def bfs(a,b,c):
    global min_cnt

    q=deque()
    q.append((a,b,c,0)) #0은 공격횟수
    visited[a][b][c] = True

    while q:
        a,b,c,cnt = q.popleft()

        if a==0 and b==0 and c==0:
            min_cnt = cnt
            return

        for at in permutations(attack):
            na = max(0, a-at[0]) #빼다보면 음수가 될 수 있음 그럴경우 방문 배열에서 에러남
            nb = max(0, b-at[1])
            nc = max(0, c-at[2])
            if not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                q.append((na,nb,nc,cnt+1))

bfs(power[0],power[1],power[2])
print(min_cnt)