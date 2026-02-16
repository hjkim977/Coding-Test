def solution(a, b, n):
    cnt=0
    while n>=a:
        remain=n%a
        n=(n//a)*b
        cnt+=n
        n+=remain
    return cnt