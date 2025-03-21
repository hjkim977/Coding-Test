def solution(arr):
    answer=[]
    answer.append(arr[0])
    
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            answer.append(arr[i+1])
    return answer

1,1,3,3,0,1,2 // 1,3,0,1,