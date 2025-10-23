def solution(my_string, num1, num2):
    answer = ''
    for index in range(len(my_string)):
        if index== num1:
            answer += my_string[num2]
        elif index == num2:
            answer += my_string[num1]
        else:
            answer += my_string[index]
    return answer
        