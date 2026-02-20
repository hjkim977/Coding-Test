#수정 전(틀린거)
#def solution(strings, n):
#    return sorted(strings, key=lambda x:x[n])

#수정 후
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x)) #n번째 문자가 같을 경우에는 전체 문자열을 기준으로 2차 정렬
