from collections import deque

def solution(cards1, cards2, goal):
    cards1=deque(cards1)
    cards2=deque(cards2)
    goal=deque(goal)
    
    while goal:
        if cards1 and cards1[0]==goal[0]: #카드1이 있고 카드1[0]과 goal[0] 같으면
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0]==goal[0]: #카드2이 있고 카드2[0]과 goal[0] 같으면
            cards2.popleft()
            goal.popleft()
        else:
            break
        
    if not goal:
        return "Yes"
    else:
        return "No"