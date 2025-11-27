while True:
    s=input()
    stack=[]

    if s=='.':
        break

    for word in s:
        if word=='(' or word=='[':
            stack.append(word)
        elif word==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(word)
        elif word==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(word)

    if stack:
        print('no')
    else:
        print('yes')