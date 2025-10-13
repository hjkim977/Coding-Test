def solution(arr):
    stack = []
    for a in arr:
        if len(stack)==0 or stack[-1]!=a:
            stack.append(a)
    return stack