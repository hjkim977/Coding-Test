def solution(n):
    a=0
    for i in range(1,n+1):
        if n%i==0:
            a+=1
    return a