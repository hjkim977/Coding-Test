def solution(s):
    answer = 0
    word = s.split(" ")
    for i in range(len(word)):
        if word[i]=="Z":
            answer-=int(word[i-1])
        else:
            answer+=int(word[i])
    return answer