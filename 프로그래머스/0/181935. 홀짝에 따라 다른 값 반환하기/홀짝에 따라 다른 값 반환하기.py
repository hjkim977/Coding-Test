def solution(n):
    l=[]
    if n%2==0:
        for i in range(2,n+1,2):
            l.append(i**2)
    else:
        for i in range(1,n+1,2):
            l.append(i)
    return sum(l)