def solution(myString):
    alp = 'abcdefghijk'
    answer = ''
    for s in myString:
        if s in alp:
            answer+='l'
        else:
            answer+=s
    return answer