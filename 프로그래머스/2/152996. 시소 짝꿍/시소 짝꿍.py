from collections import Counter
def solution(weights):
    result = 0
    
    #1:1일 때
    dic = Counter(weights) #{"100":2,"180":1,"270":1,"360":1}
    for key,value in dic.items():
        if value>=2:
            result+= value*(value-1)//2
    
    weights = set(weights)
    
    # 2:3,2:4,3:4
    for w in weights:
        if w*2/3 in weights:
            result += dic[w*2/3]*dic[w]
        if w*2/4 in weights:
            result += dic[w*2/4]*dic[w]
        if w*3/4 in weights:
            result += dic[w*3/4]*dic[w]
    return result