def solution(my_string, over, s):
    l=len(over)
    answer = my_string[:s]+over+my_string[s+l:]
    return answer