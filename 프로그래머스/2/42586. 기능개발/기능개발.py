def solution(pro, speeds):
    answer = []
    days = []
    queue = []
    
    for i in range(len(pro)):
        remain=100-pro[i]
        if remain%speeds[i]==0:
            days.append(remain//speeds[i])
        else:
            days.append(remain//speeds[i]+1)

    for i in range(len(days)):
        if len(queue)==0 or queue[0]>=days[i]:
            queue.append(days[i])
        else:
            answer.append(len(queue))
            queue.clear()
            queue.append(days[i])       
    answer.append(len(queue))
                           
    return answer