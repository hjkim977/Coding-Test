def solution(n):
    l=[]
    l.append(n)
    while n!=1:
        if n%2==0:
            n=n//2
            l.append(n)
        else:
            n=n*3+1
            l.append(n)
    return l