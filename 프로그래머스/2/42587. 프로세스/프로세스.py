from collections import deque

def solution(priorities, location):
    p = []
    for i,j in enumerate(priorities):
        p.append((i,j))
    q=deque(p)
    order=0
    
    
    while q:
        higher=False
        process=q.popleft()
        
        for wait in q:
            if process[1]<wait[1]:
                higher=True
                break
                
        if higher:
            q.append(process)
        else:
            order+=1
            if location==process[0]:
                return order