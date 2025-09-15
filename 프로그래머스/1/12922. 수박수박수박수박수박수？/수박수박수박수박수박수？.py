def solution(n):
    answer = ''
    while n>0:
        if n%2!=0: #홀수
            answer += '수'
        else:
            answer += '박'
        n-=1
    if n%2==0:
        answer = answer[::-1]
    return answer