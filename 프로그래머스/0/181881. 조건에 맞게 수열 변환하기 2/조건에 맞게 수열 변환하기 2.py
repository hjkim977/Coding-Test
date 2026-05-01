def solution(arr) : 
    answer=0
    old=arr
    while 1: 
        new=[]
        for i in old : 
            if i>= 50 and i%2==0:
                i=i/2
            elif i<50 and i%2!=0 : 
                i=i*2+1
            new.append(int(i))
        if old==new: 
            break
        else: 
            old=new
            answer+=1
    return answer