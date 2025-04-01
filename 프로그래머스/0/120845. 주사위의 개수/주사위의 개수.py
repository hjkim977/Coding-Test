def solution(box, n):
    # 각 방향별로 주사위를 몇 개씩 넣을 수 있는지 계산
    count_x = box[0] // n
    count_y = box[1] // n
    count_z = box[2] // n
    
    # 총 가능한 주사위 개수
    return count_x * count_y * count_z