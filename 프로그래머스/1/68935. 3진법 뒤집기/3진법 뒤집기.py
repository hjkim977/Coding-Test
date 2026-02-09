def solution(n):
    a=''
    while 1:
        if n==0:
            break
        nmg=n%3
        n=n//3
        a+=str(nmg)
    
    return int(a,3)