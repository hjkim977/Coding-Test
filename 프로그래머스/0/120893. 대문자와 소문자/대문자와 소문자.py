def solution(s):
    answer = ''
    for i in s:
        if i.islower():
            answer+=i.upper()
        else:
            answer+=i.lower()
    return answer