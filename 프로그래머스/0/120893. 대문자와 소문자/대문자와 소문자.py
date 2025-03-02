def solution(s):
    answer = ''
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            answer+=i.upper()
        else:
            answer+=i.lower()
    return answer