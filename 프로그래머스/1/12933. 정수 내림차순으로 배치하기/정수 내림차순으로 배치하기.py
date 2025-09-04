def solution(n):
    n=str(n)
    a=[]
    for i in n:
        a.append(i)
    a.sort(reverse=True)
    return int(''.join(a))