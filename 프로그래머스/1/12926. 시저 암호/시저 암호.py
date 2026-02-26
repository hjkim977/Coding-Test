def solution(s, n):
    result=''
    for c in s:
        if c==' ':
            result+=' '
        elif c.isupper():
            a=chr((ord(c)-ord('A')+n)%26+ord('A'))
            result+=a
        elif c.islower():
            a=chr((ord(c)-ord('a')+n)%26+ord('a'))
            result+=a
    return result