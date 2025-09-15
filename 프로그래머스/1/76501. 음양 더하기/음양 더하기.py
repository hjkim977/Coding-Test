def solution(absolutes, signs):
    answer = 0

    for k,v in zip(absolutes,signs):
        if v==True:
            answer += k
        else:
            answer -= k
    return answer