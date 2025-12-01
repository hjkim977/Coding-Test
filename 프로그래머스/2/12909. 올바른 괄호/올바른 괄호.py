def solution(s):
    stack=[]
    
    for i in s:
        if stack==[] or i=='(':
            stack.append(i)
        elif stack[0]=='(' and i==')':
            stack.pop()
    if stack:
        return False
    else:
        return True
        