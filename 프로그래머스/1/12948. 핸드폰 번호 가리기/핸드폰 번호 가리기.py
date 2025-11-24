def solution(phone_number):
    ma = '*'*(len(phone_number)-4)
    nma = phone_number[len(ma)::]
    return ma+nma