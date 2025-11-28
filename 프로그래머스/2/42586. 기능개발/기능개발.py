def solution(progresses, speeds):
    works=[] #작업
    stack=[]
    answer=[]
    
    for idx in range(len(progresses)):
        remain=100-progresses[idx]
        if remain%speeds[idx]==0:
            works.append(remain//speeds[idx])
        else:
            works.append(remain//speeds[idx]+1)
    
    for i in range(len(works)):
        if stack==[] or stack[0]>=works[i]:
            stack.append(works[i])
        else:
            answer.append(len(stack))
            stack=[]
            stack.append(works[i])
        
    if stack:
        answer.append(len(stack))
    return answer