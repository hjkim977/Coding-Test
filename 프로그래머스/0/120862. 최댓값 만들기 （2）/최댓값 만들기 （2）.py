def solution(numbers):
    numbers.sort()
    f=numbers[0]*numbers[1]
    b=numbers[-1]*numbers[-2]
    if f>=b:
        return f
    return b