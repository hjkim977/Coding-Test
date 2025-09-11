def solution(name, yearning, photo):
    result = []
    person = dict(zip(name,yearning))
    
    for i in photo:
        score = 0
        for j in i:
            if j in person:
                score += person[j]
        result.append(score)
    
    return result