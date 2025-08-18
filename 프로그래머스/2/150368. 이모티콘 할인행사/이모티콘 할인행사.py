from itertools import product

def solution(users, emoticons):
    answer = [0,0] # 가입자 수, 이모티콘 매출액
    events = [10,20,30,40] # 이모티콘 할인율
    m = len(emoticons) #이모티콘의 개수
    
    for event in product(events,repeat=m): #중복 순열, 이모티콘 개수만큼 할인율 만듦
        sign_up,total = 0,0 # 가입자 수, 판매액
        
        for ratio, limit in users:
            price = 0  # 유저마다 초기화
            for emo, sale in zip(emoticons, event):
                if sale >= ratio:  # 원하는 할인율 이상이면 구매
                    price += emo * (100 - sale) // 100
            if price >= limit:  # 플러스 가입
                sign_up += 1
            else:  # 그냥 구매 금액만 합산
                total += price
        
        if sign_up > answer[0] or sign_up==answer[0] and total > answer[1]:
            answer = [sign_up,total]

    return answer