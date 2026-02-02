def solution(s):
    answer = []
    position = {}
    
    for i in range(len(s)):
        if s[i] not in position:
            position[s[i]]=i
            answer.append(-1)
        else:
            a = i-position[s[i]]
            answer.append(a)
            position[s[i]]=i
    return answer