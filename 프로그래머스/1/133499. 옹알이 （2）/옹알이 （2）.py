def solution(babbling):
    cnt=0
    talk=["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for t in talk:
            if t*2 not in b:
                b=b.replace(t," ")
        if b.isspace():
            cnt+=1
    return cnt