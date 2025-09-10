def solution(t, p):
    result = 0

    for n in range(len(t)):
        word = t[n:n+len(p)]   
        if word <= p and len(word)==len(p):
            result+=1 
    return result