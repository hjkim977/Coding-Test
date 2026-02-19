def solution(k, m, score):
    cost=0
    score.sort(reverse=True)
    
    for i in range(0,len(score),m):
        if len(score[i:i+m])==m:
            cost+=min(score[i:i+m])*m
    return cost