def solution(s):
    a=sorted(s)
    answer=''
    for i in a[::-1]:
        answer+=i
    return answer