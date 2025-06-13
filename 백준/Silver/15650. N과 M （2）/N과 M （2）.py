n,m = map(int,input().split())
visited = [False]*(n+1)
result = []

def backtrack():
    if len(result)==m:
        print(" ".join(map(str,result)))
        return

    for i in range(1,n+1):
        if not visited[i] and len(result)==0 or result[-1]<i:
            visited[i] = True
            result.append(i)
            backtrack()
            result.pop()
            visited[i] = False

backtrack()