def solution(price, money, count):
    num=0
    total=0
    
    while 1:
        num+=1
        total+=price*num
        
        if num==count:
            if money-total>=0:
                return 0
            else:
                return total-money