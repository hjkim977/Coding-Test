def solution(s, p):
    l=[]
    w=''
    for i in s:
        w+=i
        l.append(w)
    if p in l:
        return 1
    return 0