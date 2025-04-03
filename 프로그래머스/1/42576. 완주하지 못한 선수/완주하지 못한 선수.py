def solution(participant, completion):
    hash={} #해시테이블 설정, 딕셔너리로 해시를 표현
    
    for p in participant:
        if p in hash:
            hash[p]+=1
        else:
            hash[p]=1
    
    for c in completion:
        hash[c]-=1
    
    for key,value in hash.items():
        if value>0:
            return key