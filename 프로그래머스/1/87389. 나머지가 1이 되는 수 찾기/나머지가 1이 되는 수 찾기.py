def solution(n):
    answer = 0
    x=2
    while x<n:
        if n%x==1:
            return x
            break
        x+=1