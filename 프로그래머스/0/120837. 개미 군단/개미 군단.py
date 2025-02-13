def solution(hp):
    a=[5,3,1]
    c=0
    for i in a:
        m=hp//i
        c+=m
        hp=hp%i
    return c