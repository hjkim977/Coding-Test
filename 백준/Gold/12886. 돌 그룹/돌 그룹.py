from collections import deque
a,b,c=map(int,input().split())
total=a+b+c

if (total%3)!=0:
    print(0)
    exit()

visited=[[0]*1501 for _ in range(1501)]

def bfs():
    q=deque()

    a1,b1 = sorted([a,b])
    c1 = total-a1-b1
    q.append((a1,b1))
    visited[a1][b1]=1

    while q:
        x,y=q.popleft()
        z=total-x-y

        if x==y==z:
            print(1)
            exit()

        for i, j in [(x,y),(x,z),(y,z)]:
            if i==j:
                continue

            small = min(i, j)
            big = max(i, j)

            new_small = small + small
            new_big = big - small
            new_third = total - new_small - new_big

            next_state = sorted([new_small, new_big, new_third])
            a2, b2 = next_state[0], next_state[1]

            if not visited[a2][b2]:
                visited[a2][b2] = True
                q.append((a2, b2))

    print(0)  # 모든 경우 탐색했는데 실패

bfs()