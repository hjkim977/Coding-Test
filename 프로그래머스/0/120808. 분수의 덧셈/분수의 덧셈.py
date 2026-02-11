def solution(numer1, denom1, numer2, denom2):
    m=denom1*denom2
    j=numer1*denom2 + numer2*denom1
    
    for i in range(m,0,-1):
        if m%i==0 and j%i==0:
            return [j//i,m//i]
            break