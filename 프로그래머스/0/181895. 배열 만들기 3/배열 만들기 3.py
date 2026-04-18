def solution(arr, intervals):
    answer = []
    for interval in intervals:
        f,b=interval[0],interval[1]
        for i in arr[f:b+1]:
            answer.append(i)
    return answer