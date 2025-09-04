def solution(x, n):
    answer = []
    total = x
    while len(answer)<n:
        answer.append(total)
        total += x
    return answer