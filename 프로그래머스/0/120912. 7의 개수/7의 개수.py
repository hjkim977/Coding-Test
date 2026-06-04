def solution(array):
    answer = 0
    for i in array:
        seven=str(i)
        answer+=seven.count("7")
    return answer