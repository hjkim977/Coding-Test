def solution(s):
    result=0
    n=len(s)
    for i in range(n):
        stack=[]
        for j in range(n):
            c=s[(i+j)%n] #회전을 표현
            if c=="(" or c=="[" or c=="{":
                stack.append(c)
            else:
                if not stack: #스택이 비어있다면 즉, 매칭되는 열린 괄호가 없다면
                    break
            
                if c==")" and stack[-1]=="(":
                    stack.pop()
                    
                elif c=="]" and stack[-1]=="[":
                    stack.pop()  

                elif c=="}" and stack[-1]=="{":
                    stack.pop()
                    
                else:
                    break
        else:
            if not stack:
                result+=1
                
    return result     