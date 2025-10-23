def solution(x):
    num = 0
    for h in str(x):
        num+=int(h)
    if x%num==0:
        return True
    else:
        return False