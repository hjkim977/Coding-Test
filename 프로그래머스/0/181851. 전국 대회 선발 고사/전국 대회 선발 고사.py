def solution(rank, attendance):
    result = []

    for idx, val in enumerate(rank):
        if attendance[idx] == True:
            result.append([rank[idx], idx]) # 등수 & 번호

    result.sort()

    a = result[0][1]
    b = result[1][1]
    c = result[2][1]

    return 10000 * a + 100 * b + c