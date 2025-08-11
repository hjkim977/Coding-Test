def solution(s):
    answer=len(s)
    
    for size in range(1,len(s)//2+1):
        cnt = 1
        press = 0
        
        cut = s[:size]
        for i in range(size,len(s),size):
            current = s[i:i+size]
            if cut==current:
                cnt += 1
            else:
                press += len(cut)
                if cnt > 1:
                    press += len(str(cnt))
                cut = current
                cnt = 1
        press += len(cut)
        if cnt > 1:
            press+=len(str(cnt))
        answer = min(answer,press)
    return answer