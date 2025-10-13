def solution(participant, completion):
    h = {}
    for p in participant:
        if p in h.keys():
            h[p]+=1
        else:
            h[p]=1
    
    answer = []
    
    for c in completion:
        if c in h.keys():
            h[c]-=1

    for k,v in h.items():
        if v>0:
            answer.append(k)
    return ",".join(answer)