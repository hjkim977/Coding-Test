from collections import Counter
def solution(clothes):
    '''category=Counter(clothes) 이렇게하면 타입 에러남 -> clothes가 리스트 형태이고 리스트는 해시로 할 수 없기 때문'''
    category=Counter([value for _,value in clothes]) #의상의 종류를 기준
    
    result=1
    for value in category.values():
        result*=(value+1)
    return result-1 #아무것도 안입는 경우 1을 빼줌