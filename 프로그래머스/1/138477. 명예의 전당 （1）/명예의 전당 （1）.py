def solution(k, score):
    answer=[]
    hof=[]
    
    for s in score:
        if len(hof)<k:
            hof.append(s)
            answer.append(min(hof))
        else:
            hof.sort()
            if hof[0]<=s:
                hof[0]=s
            answer.append(min(hof))
    return answer
            

#     for h in hof:
#         if len(answer)>=1:
#             answer.append(min(answer))
#         else:
#             answer.append(h)
            
#     for s in score[k:]:
#         if s>min(hof):
#             hof.remove(min(hof))
#             hof.append(s)
#         answer.append(min(hof))
#     return answer