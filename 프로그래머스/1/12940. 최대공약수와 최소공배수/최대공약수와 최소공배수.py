def solution(n, m):
    answer = [1,n*m]
    for i in range(2,n+1): # 최대 공약수
        if n%i==0 and m%i==0:
            answer[0]=i
    # 최소 공배수
    a,b = min(n,m),max(n,m)
    for i in range(b,b*a+1,b):
        for j in range(1,b+1):
            if a*j==i:
                answer[1] = min(answer[1],a*j)
    return answer
    