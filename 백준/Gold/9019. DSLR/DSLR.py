#bfs
'''어떤 명령어를 조합하면 s->e로 갈 수 있을지를 찾는 문제이기 때문에
가능한 모든 연산을 하나씩 시도해야함
=> D,S,L,R 네가지 연산 전부 해야함 '''

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visited = [False] *10001
    q=deque()
    q.append((s,''))
    visited[s] = True

    while q:
        n,order = q.popleft()
        if n==e:
            print(order)
            return #bfs함수만 종료

        # D
        nn = (n * 2) % 10000
        if not visited[nn]:
            visited[nn] = True
            q.append((nn, order + "D"))

        # S
        nn = n - 1 if n != 0 else 9999
        if not visited[nn]:
            visited[nn] = True
            q.append((nn, order + "S"))

        # L
        nn = (n % 1000) * 10 + (n // 1000)
        if not visited[nn]:
            visited[nn] = True
            q.append((nn, order + "L"))

        # R
        nn = (n % 10) * 1000 + (n // 10)
        if not visited[nn]:
            visited[nn] = True
            q.append((nn, order + "R"))

t = int(input())
for _ in range(t):
    s,e = map(int,input().split())
    bfs()