def solution(my_string):
    a=0
    num=''
    for i in my_string:
        if i.isdigit():
            num+=i
        else:
            if num!='':
                a+=int(num)
                num=''
    if num!='':
        a+=int(num)
    return a