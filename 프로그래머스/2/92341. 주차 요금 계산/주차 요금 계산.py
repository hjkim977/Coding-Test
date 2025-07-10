from math import ceil

def solution(fees, records):
    car = {} # 차번호 -> 입차시간(분)
    total = {} # 주차 누적시간을 저장
    result = {}
    
    for record in records:
        time,num,log = record.split()
        h,m = time.split(':')
        minutes = int(h)*60+int(m)
        
        if log == "IN":        
            car[num] = minutes
        
        else:
            in_time = car.pop(num)
            total_time = minutes - in_time
            total[num] = total.get(num, 0) + total_time
            
    for num, in_time in car.items(): #out이면 car에 있는 minutes값이 없어질텐데 있다는건 out이 없다는 얘기
        total_time = (23*60+59) - in_time
        total[num] = total.get(num,0) + total_time
        
    default_time,default_fee,over_time,over_fee = fees    
    for num in total:
        if total[num]<=default_time : #누적 주차시간이 기본시간보다 작을때
            result[num] = default_fee
        else:
            result[num] = default_fee+ceil((total[num]-default_time)/over_time)*over_fee
    
    answer = [fee for key,fee in sorted(result.items())]
    
    return answer