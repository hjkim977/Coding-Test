def solution(numbers):
    answer=[]
    for a in range(len(numbers)-1):
        for b in range(a+1,len(numbers)):
            sum_numbers=numbers[a]+numbers[b]
            if sum_numbers not in answer:
                answer.append(sum_numbers)
    answer.sort()
    return answer