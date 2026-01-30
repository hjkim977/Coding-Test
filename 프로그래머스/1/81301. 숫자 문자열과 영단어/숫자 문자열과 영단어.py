def solution(s):
    table=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(10):
        s=s.replace(table[i],str(i))
        
    return int(s)