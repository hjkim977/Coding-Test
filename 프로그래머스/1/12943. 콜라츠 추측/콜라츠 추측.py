def solution(n):
    cnt = 0
    while 1:
        if n==1:
            return cnt
        
        elif cnt>=500 and n!=1:
            return -1

        if n%2==0: #짝수
            n = n//2
            cnt+=1
        else:
            n = n*3+1 
            cnt+=1