def solution(nums):
    monster=len(set(nums))
    num=len(nums)//2 #가져가도 되는 개수
    return min(monster, num)