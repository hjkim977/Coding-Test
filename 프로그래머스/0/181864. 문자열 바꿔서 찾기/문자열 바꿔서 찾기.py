def solution(myString, pat):
    c=''
    for i in myString:
        if i=='A':
            c+='B'
        elif i=='B':
            c+='A'
    if pat in c:
        return 1
    return 0