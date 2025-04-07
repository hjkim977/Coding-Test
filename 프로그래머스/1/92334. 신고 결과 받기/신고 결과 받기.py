from collections import defaultdict
def solution(id_list, report, k):
    result=[0]*len(id_list)
    report=set(report)
    
    reported=defaultdict(set) #신고당한 사람
    report_id=defaultdict(set) #내가 누굴 신고했는지
    
    for i in report:
        a,b=i.split()
        reported[b].add(a)
        report_id[a].add(b)

    s=set() # k번 이상 신고당해서 중지
    for i,j in reported.items(): 
        if len(j)>=k:
            s.add(i)
    # s = {i for i, j in reported.items() if len(j) >= k}

    for i, user in enumerate(id_list): # 내가 신고한 사람들 중 정지된 사람 수 만큼 메일 받음 / 인덱스랑 같이 저장하는 함수
        result[i] = len(report_id[user] & s)
    return result