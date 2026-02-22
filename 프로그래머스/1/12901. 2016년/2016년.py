def solution(a, b):
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    d=0
    for i in range(a-1):
        d+=month[i]
    d+=b
    return day[d%7]