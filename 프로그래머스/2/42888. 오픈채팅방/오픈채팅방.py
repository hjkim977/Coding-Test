def solution(record):
    result = []
    user = {}  # uid -> 닉네임
    logs = []  # (메시지종류, uid)

    for i in record:
        w = i.split()
        message = w[0]
        uid = w[1]
        
        if message in ["Enter", "Change"]:
            nickname = w[2]
            user[uid] = nickname  # 항상 최신 닉네임 저장
        
        if message in ["Enter", "Leave"]:
            logs.append((message, uid))  # 순서대로 저장
    
    for message, uid in logs:
        nickname = user[uid]
        if message == "Enter":
            result.append(f"{nickname}님이 들어왔습니다.")
        elif message == "Leave":
            result.append(f"{nickname}님이 나갔습니다.")
    
    return result
