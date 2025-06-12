def backtrack(k, c, dungeons, visited):
    max_c = c
    for i in range (len(dungeons)):
        
        if not visited[i]:
            need, use = dungeons[i]
            if k>=need:
                visited[i] = True
                max_c = max(max_c,backtrack(k-use, c+1, dungeons, visited))
                visited[i] = False
    return max_c
    
def solution(k, dungeons):
    visited = [False]*len(dungeons)
    return backtrack(k, 0, dungeons, visited)