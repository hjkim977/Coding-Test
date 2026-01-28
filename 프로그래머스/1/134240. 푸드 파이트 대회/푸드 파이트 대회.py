def solution(food):
    half=''
    dic={}
    for f in range(1,len(food)):
        dic[f]=food[f]//2
    for k,v in dic.items():
        half+=str(k)*v
    return half+'0'+half[::-1]