from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1),deque(queue2)
    sum1,sum2 = sum(q1),sum(q2)
    target = (sum1+sum2)//2
    cnt = 0
    limit = len(q1)*3
    while cnt<limit:
        if target==sum1:
            return cnt
        if sum1>target:
            x = q1.popleft()
            sum1-=x
            q2.append(x)
            sum2+=x
        else:
            x = q2.popleft()
            sum2-=x
            q1.append(x)
            sum1+=x
        cnt+=1
    return -1