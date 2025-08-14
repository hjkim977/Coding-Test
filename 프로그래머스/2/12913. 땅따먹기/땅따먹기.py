#dp
def solution(land):
    for i in range(1,len(land)): #0행은 이전 행이 존재하지 않아서 1부터 시작
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] +land[i-1][j+1:])
    return max(land[len(land)-1]) #누적된 값들 중 제일 큰 값 출력