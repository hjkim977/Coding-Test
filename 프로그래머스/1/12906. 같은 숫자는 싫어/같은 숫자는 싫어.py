def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for a in range(1,len(arr)):
        if answer[-1]!=arr[a]:
            answer.append(arr[a])
    return answer