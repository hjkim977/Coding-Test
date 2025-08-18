def solution(survey, choices):
    result = ''
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3,}
    char = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(choices)):
        f,b = survey[i]
        c = choices[i]
        if c<4:
            char[f]+=score[c]
        elif c>4:
            char[b]+=score[c]
    
    if char['R']>=char['T']:
        result+='R'
    elif char['R']<char['T']:
        result+='T'  
    if char['C']>=char['F']:
        result+='C'
    elif char['C']<char['F']:
        result+='F'
    if char['J']>=char['M']:
        result+='J'
    elif char['J']<char['M']:
        result+='M'
    if char['A']>=char['N']:
        result+='A'
    elif char['A']<char['N']:
        result+='N'
        
    return result