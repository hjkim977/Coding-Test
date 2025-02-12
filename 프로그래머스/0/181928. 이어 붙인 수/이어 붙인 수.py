def solution(num_list):
    o=[]
    e=[]
    for i in num_list:
        if i%2!=0:
            o.append(str(i))
        else:
            e.append(str(i))
    return int("".join(o))+int("".join(e))