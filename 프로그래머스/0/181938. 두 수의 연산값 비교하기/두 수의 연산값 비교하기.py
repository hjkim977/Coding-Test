def solution(a, b):
    s=str(a)+str(b)
    m=2*a*b
    if int(s)>int(m):
        return int(s)
    else:
        return int(m)