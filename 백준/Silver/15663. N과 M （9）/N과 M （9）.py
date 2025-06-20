import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))
visited = [False]*n

choose = []
result = set()

def backtrack():
    if len(choose) == m:
        result.add(tuple(choose))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            choose.append(nums[i])
            backtrack()
            choose.pop()
            visited[i] = False

backtrack()

for i in sorted(result):
    print(' '.join(map(str,i)))