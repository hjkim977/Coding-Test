def solution(l, r):
    answer=[]
    for i in range(l,r+1):
        if set(str(i)) <= {'0','5'}: #집합 포함관계
            answer.append(i)
    if answer==[]:
        return [-1]
    return answer