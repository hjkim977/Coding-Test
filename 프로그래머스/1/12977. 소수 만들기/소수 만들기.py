def solution(nums):
    nums.sort()
    result = 0
    
    def find(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1): #range는 정수만 받아서 int를 꼭 해줘야함
            if n%i==0: #소수 아님
                return False
        return True
        
    
    def backtrack(arr, start, pick):
        nonlocal result #solution 내부 지역변수라서 nonlocal
        
        if pick==3:
            total = sum(arr)
            if find(total):
                result += 1
            return
                
        for i in range(start,len(nums)):
            arr.append(nums[i])
            backtrack(arr,i+1,pick+1)
            arr.pop()
            
    backtrack([],0,0)
    return result