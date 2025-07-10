# 가장 먼 곳부터 처리하기
def update(box, cap):
    while len(box):
        if cap<box[-1]:
            box[-1]-= cap
            break
        else:
            cap -= box[-1]
            box.pop() # box[-1]==0이 되니까 pop이됨
    
def solution(cap, n ,deliveries, pickups):
    answer = 0
    
    while len(deliveries) or len(pickups):
        while deliveries and deliveries[-1]==0:
            deliveries.pop() # 맨오른쪽에 있는 0을 제거함
        while pickups and pickups[-1]==0:
            pickups.pop() # 맨오른쪽에 있는 0을 제거함
        
        answer += max(len(deliveries),len(pickups)) * 2
        update(deliveries, cap)
        update(pickups, cap)
    
    return answer