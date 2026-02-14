def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        s=[]
        for j in range(len(arr1[0])):
            s.append(arr1[i][j]+arr2[i][j])
        answer.append(s)
    return answer