def solution(numlist, n):
    answer = []
    for i in range(10000):
        if(n+i in numlist):
            answer.append(n+i)
        if(i!=0 and n-i in numlist):
            answer.append(n-i)
    return answer