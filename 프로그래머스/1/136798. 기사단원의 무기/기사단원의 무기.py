def solution(number, limit, power):
    measure = []
    for i in range(1,number+1):
        a=0
        for j in range(1,int(i**0.5)+1): 
            if i%j ==0: 
                a+=1 
                if j**2 != i:
                    a+=1
        if a> limit:
            a = power
        measure.append(a)
    return sum(measure)