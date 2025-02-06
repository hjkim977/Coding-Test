def solution(n):
    total=0
    for k in range(n+1):
        if k%2==0:
            total+=k
    return total