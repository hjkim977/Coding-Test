#bfs
import sys
from collections import deque
input=sys.stdin.readline

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

t=int(input())
for _ in range(t):
    store_count = int(input())
    home = tuple(map(int,input().split()))
    store = [tuple(map(int,input().split())) for _ in range(store_count)]
    festival = tuple(map(int,input().split()))

    visited = [False]*store_count #편의점 방문 여부만 체크

    def bfs():
        q = deque([home])

        while q:
            x,y = q.popleft()

            if distance((x,y),festival)<=1000: #현재 위치에서 페스티벌까지 거리가 1000m 이하면 happy
                return True

            for i in range(store_count):
                if not visited[i] and distance((x, y), store[i]) <= 1000:
                    visited[i] = True
                    q.append(store[i])

        return False

    print("happy" if bfs() else "sad")