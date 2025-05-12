from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().strip().split())
visited=[-1]*100001
count=[0]*100001
q=deque()

def bfs():
    q.append(n)
    visited[n]=0
    count[n]=1

    while q:
        current=q.popleft()

        for next in [current-1,current+1,current*2]:
            if 0<=next<100001:
                if visited[next]==-1:
                    visited[next]=visited[current]+1
                    count[next]=count[current]
                    q.append(next)
                elif visited[next]==visited[current]+1:
                    count[next]+=count[current]
    print(visited[k])
    print(count[k])

if n==k:
    print(0)
    print(1)
else:
    bfs()