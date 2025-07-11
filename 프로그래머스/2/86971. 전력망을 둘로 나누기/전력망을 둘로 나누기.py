# bfs
from collections import deque
def bfs(tree,start,cnt,n):
    visited = [False]*(n+1)
    q = deque([start])
    visited[start] = True
    cnt+=1
    
    while q:
        node = q.popleft()
        for connect in tree[node]:
            if not visited[connect]:
                q.append(connect)
                visited[connect] = True
                cnt+=1
    return cnt
                
def solution(n, wires):
    min_count = float('inf')
    
    for i in range(len(wires)):
        tree = [[] for _ in range(n+1)]
        cut_wires = wires[:i]+wires[i+1:]
    
        for wire in cut_wires: #연결
            tree[wire[0]].append(wire[1])
            tree[wire[1]].append(wire[0])
            
        cnt = bfs(tree,1,0,n)
        diff = abs(cnt - (n-cnt))
        min_count = min(diff,min_count)
    return min_count

'''
1. 하나를 끊은 전선들이 어떻게 연결되어 있는지
2. '''