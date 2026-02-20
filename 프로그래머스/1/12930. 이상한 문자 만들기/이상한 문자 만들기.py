def solution(s):
    answer=[]
    words=s.split(' ')
    for word in words:
        w=''
        for a in range(len(word)):
            if a%2==0:
                w+=word[a].upper()
            else:
                w+=word[a].lower()
        answer.append(w)
    return ' '.join(answer)