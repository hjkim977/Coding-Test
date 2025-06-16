def solution(num, k):
    num = str(num)
    k = str(k)
    for a,b in enumerate(num):
        if b==k:
            return int(a)+1
    return -1