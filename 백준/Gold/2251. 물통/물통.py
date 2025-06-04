import sys
from collections import deque
input = sys.stdin.readline

a,b,c = map(int, input().split())
#변경할 수 있는 경우 총 6가지: a->b, a->c....
visited = [[False]*(b+1) for _ in range(a+1)]
result = []

q=deque()
q.append((0,0))
visited[0][0]=True

#x,y의 경우의 수 저장장
def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x,y))

def bfs():
    while q:
        #x는 a에 들어있는 물의 양, y는 b에 들어있는 물의 양
        x,y = q.popleft()
        z = c-x-y

        #a물통이 비어있는 경우 c물통에 남아있는 양 저장
        if x==0:
            result.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x - water, y + water)

        # x -> z
        water = min(x, c-z)
        pour(x - water, y)

        # y -> x
        water = min(y, a-x)
        pour(x + water, y - water)

        # y -> z
        water = min(y, c-z)
        pour(x, y - water)

        # z -> x
        water = min(z, a-x)
        pour(x + water, y)

        # z -> y
        water = min(z, b-y)
        pour(x, y + water)

bfs()

result.sort()
for i in result:
    print(i, end=" ")