def solution(myString, pat):
    answer = 0
    for num in range(0,len(myString)-len(pat)+1,1):
        if myString[num:num+len(pat)]==pat:
            answer+=1
    return answer