import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,a,b=map(int,input().split())
cave = [[] for _ in range(n+1)] #인접리스트 만듦
visited = [0]*(n+1)

total = 0 #우리가 구해야되는 것
for _ in range(n-1):
    r1,r2,l = list(map(int,input().split()))
    cave[r1].append((r2,l))
    cave[r2].append((r1,l))

def dfs(start, target, total, max_line):
    visited[start]=1
    if start==target:
        print(total-max_line)
        exit(0)

    for next,line in cave[start]:
        if not visited[next]:
            dfs(next, target, total+line, max(max_line, line))

dfs(a, b, 0, 0)