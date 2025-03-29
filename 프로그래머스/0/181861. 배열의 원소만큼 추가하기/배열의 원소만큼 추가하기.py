def solution(arr):
    answer = []
    for i in arr:
        answer.extend([i]*int(i))
    return answer