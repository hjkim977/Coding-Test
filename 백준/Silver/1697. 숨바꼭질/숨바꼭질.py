from collections import deque

n,k=map(int,input().split())

def bfs(n,k):
    q=deque([n])

    max_range=100001 #위치가 0~100,000까지라서
    visited=[0]*max_range

    while q:
        current=q.popleft()

        if current==k:
            return visited[current]
        
        for next_pos in (current-1, current+1, current*2):
            if 0<=next_pos<max_range and visited[next_pos]==0:
                visited[next_pos]=visited[current]+1
                q.append(next_pos)

print(bfs(n,k))