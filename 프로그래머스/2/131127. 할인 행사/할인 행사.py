from collections import Counter
def solution(want, number, discount):
    days=0 #할인 받을 수 있는 총 일수
    product={}
    
    for i in range(len(want)): #want와 number을 합침
        product[want[i]]=number[i] #product = dict(zip(want, number))
    
    for i in range(len(discount)):
        member=Counter(discount[i:10+i])
        if product==member:
            days+=1
    return days