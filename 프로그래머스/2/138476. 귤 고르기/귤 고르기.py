# 개수가 많은 순서대로 정렬
from collections import Counter

def solution(k, tangerine):
    dic=Counter(tangerine)
    sort_dic=sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    result=0
    for _,value in sort_dic:
        k-=value
        result+=1
        if k<=0:
            return result
    return result