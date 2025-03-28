def solution(s):
    stack=[]
    for i in s:
        if stack and stack[-1]==i:  # 스택이 비어있지 않고, top과 현재 문자가 같다면 pop
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1