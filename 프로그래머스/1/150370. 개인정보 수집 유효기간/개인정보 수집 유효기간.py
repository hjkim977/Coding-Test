def ch_date(date):
    y,m,d = date.split(".")
    y,m,d = int(y),int(m),int(d)
    return y*10000+m*100+d

def solution(today, terms, privacies):
    result = []
    dic = {}
    for term in terms: # 약관을 딕셔너리 형태로 저장
        a,b = term.split()
        dic[a]=int(b)
    
    today = ch_date(today)
    
    for p in range(len(privacies)):
        register,alp = privacies[p].split()
        y,m,d = map(int,register.split('.'))

        m+=dic[alp] # 기간 추가
        y += (m-1)//12 # 만약에 기간이 19가 되어 m=24면 년도에 1이 추가 되어야하는데 2가 추가됨 
        m = (m-1)%12+1
        d -= 1
        
        if d == 0:
            d = 28
            m -= 1
            if m == 0:
                m = 12
                y -= 1
            
        end = ch_date(f"{y:04d}.{m:02d}.{d:02d}")
        if end < today:
            result.append(p+1)

    return result    