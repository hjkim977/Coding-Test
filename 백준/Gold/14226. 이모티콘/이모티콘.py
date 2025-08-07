from collections import deque

s = int(input())
visited = [[False]*(s+1) for _ in range(s+1)]

def bfs(s):
    q = deque()
    q.append((1,0,0))
    visited[1][0] = True

    while q:
        screen,board,time = q.popleft()
        if screen == s:
            print(time)
            break
        
        # 1. 화면 -> 클립보드
        if screen <= s and not visited[screen][screen]:
            visited[screen][screen]=True
            q.append((screen,screen,time+1))

        # 2. 클립보드 -> 화면
        if board+screen<=s and board>0 and not visited[board+screen][board]:
            visited[board+screen][board]=True
            q.append((board+screen,board,time+1))

        # 3. 화면에 있는 이모티콘 하나 삭제
        if screen - 1 >= 0 and not visited[screen-1][board]:
            visited[screen-1][board]=True
            q.append((screen-1,board,time+1))          

bfs(s)