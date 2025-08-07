def rank(cnt):
    if cnt==6:
        return 1
    elif cnt==5:
        return 2
    elif cnt==4:
        return 3
    elif cnt==3:
        return 4
    elif cnt==2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    cnt = 0
    for num in lottos:
        if num!=0 and num in win_nums: #0을 제외하고 맞는 번호 개수 세기
            cnt += 1
    lower = rank(cnt)
    best = rank(cnt+zero)
    
    answer.append(best)
    answer.append(lower)
    
    return answer