def solution(numbers):
    numbers = list(map(str,numbers)) # 숫자 -> 문자열로 변환
    numbers.sort(key=lambda x : x*3, reverse=True)
    # *3으로 하는 이유 : 1000이하이기 때문에
    # 333 > 303030 이유 : 문자열 크기 비교는 사전 순으로 비교
    result = "".join(numbers)
    
    # 만약, numbers=[0,0] 일 때 0으로 출력 되어야함
    
    return str(int(result))
    
