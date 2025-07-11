def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1. 소문자로 치환
    
    change = '' # 2. 소문자, 숫자, '-','_','.'가 아니면 제외
    for s in new_id:
        if s.isalnum()==True or s in ['-','_','.']:
            change+=s
            
    while '..' in change: # 3. 마침표가 2개 이상이면 하나로 바꿈
        change = change.replace('..','.')
    
    if change[0]=='.': # 4. 앞뒤에 마침표가 있으면 제거
        change = change[1:]
    if len(change)>=1 and change[-1]=='.':
        change = change[:-1]
    
    if len(change)==0: # 5. 빈문자열이면 a 추가
        change = 'a'
        
    if len(change)>=16: # 6. 16자 글자 이상이면 15글자까지만, 끝자리가 . 이면 제거 
        change = change[:15]
        if change[-1]=='.':
            change = change[:-1]
    
    while len(change)<3: # 7. 길이가 3이 될 떄까지 마지막 글자 붙임
        change += change[-1]
    
    return change